import pickle
import numpy as np
from DbCtr import ctr
from ltp import LTP
ltp = LTP()

TBNAME = "tbnlp"

def getItem(id):
    item = None
    query = ctr.queryData(TBNAME, id)
    if query:
        item = pickle.loads(query[1])
    else:
        item = NeureCtr(id)
    return item

def smartUpDb(item):
    query = ctr.queryData(TBNAME, item.uuid)
    if query:
        ctr.updateData(TBNAME, item.uuid, pickle.dumps(item))
    else:
        ctr.insertData(TBNAME, {'id':item.uuid, 'sequence':pickle.dumps(item)})

class NeureCtr:
    def __init__(self, id):
        self._uuid = id
        self._relevants = {}

    @property
    def uuid(self):
        return self._uuid

    @property
    def relevants(self):
        return self._relevants
    @relevants.setter
    def relevants(self, value):
        if value[0] not in self._relevants:
            self._relevants[value[0]] = [value[1]]
        else:
            info = self._relevants[value[0]]
            info.append(value[1])

class DataCtr:
    def __init__(self):
        self.dict_path = 'dict_txt.txt'
        self.names_path = 'names.txt'
        self.actions_path = 'actions.txt'
        self.envir_labels_path = 'envir_labels.txt'
        self.content_label_path = 'content_labels.txt'
        self.predicate_label_path = 'predicate_label.txt'
        self.dict_txt = self.get_dict_txt(self.dict_path)

    #字典的键、值互换
    def swap_key_value(self, dic):
        keys, values = list(dic.keys()), list(dic.values())
        dic_temp = {}
        for i in range(len(keys)):
            dic_temp.update({values[i]: keys[i]})
        return dic_temp
    
    #读取文本内容并转成字典
    def get_dict_txt(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        dict_txt = eval(lines[0]) if len(lines) > 0 else {}
        return dict_txt

    #读取文本内容并转成列表
    def get_list_txt(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        list_txt = eval(lines[0]) if len(lines) > 0 else []
        return list_txt
    
    #插入新的汉字-数字对照到汉字-数字对照字典
    def insert_txt(self, txt):
        txt_temp = ''
        for s in txt:
            if s not in self.dict_txt:
                txt_temp += s
        count = len(self.dict_txt)
        for s in txt_temp:
            self.dict_txt[s] = count
            count += 1
        with open(self.dict_path, 'w', encoding='utf-8') as f:
            f.write(str(self.dict_txt))

    #从汉字-数字对照表dict_txt.txt中获取数字元组
    def get_number_tuple(self, text):
        list_data = []
        for s in text:
            list_data.append(self.dict_txt[s])
        return tuple(list_data)

    #根据数字元组获取对应汉字
    def get_txt_from_tuple(self, tuple_data):
        txt_temp = ''
        data = self.swap_key_value(self.dict_txt)
        for i in tuple_data:
            txt_temp += data[i]
        return txt_temp

    #根据标签获取对应汉字
    def get_txt_from_label(self, label, path):
        dic = self.get_dict_txt(path)
        data = self.swap_key_value(dic)
        tuple_data =data[label]
        res = self.get_txt_from_tuple(tuple_data)
        return res

    #小明教小王，小明问小王，小王回答小明
    def create_environment_txt(self):
        with open(self.names_path, 'r', encoding='utf-8') as f:
            names = list(f.readlines())
        with open(self.actions_path, 'r', encoding='utf-8') as f:
            actions = list(f.readlines())
        list_envir = []  
        count = 1     
        for name in names:
            for action in actions:
                for name2 in names:
                    envir_title = name.strip() + action.strip() + name2.strip()
                    self.insert_txt(envir_title)
                    tuple_data = self.get_number_tuple(envir_title)
                    print(envir_title, tuple_data)
                    list_envir.append([tuple_data, count])
                    count += 1
        with open(self.envir_labels_path, 'w', encoding='utf-8') as f:
            f.write(str(dict(list_envir)))

    def create_content_txt(self, content):
        return self.create_dict_txt(content, self.content_label_path)

    def create_predicate_txt(self, predicate):
        return self.create_dict_txt(predicate, self.predicate_label_path)

    def create_dict_txt(self, text, path):
        lines = self.get_dict_txt(path)
        self.insert_txt(text)        
        tuple_data = self.get_number_tuple(text)
        if tuple_data not in lines:
            lines.update({tuple_data: len(lines)})
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(lines))
        return lines[tuple_data]

    def split_sentence(self, content):
        arr = [val.strip() for val in content.split("：")]
        if len(arr) != 2:
            return
        self.insert_txt(arr[0])
        tuple_data = self.get_number_tuple(arr[0])
        envir_labels = self.get_dict_txt(self.envir_labels_path)
        envir_label = envir_labels[tuple_data]
        
        sentence = arr[1]
        seg, hidden = ltp.seg([sentence])
        srl = ltp.srl(hidden, keep_empty=False)
        item = srl[0][0] if len(srl[0]) > 0 else None
        if item and item[1][0][0] == 'A0' and item[1][1][0] == 'A1':
            content_tuple = item[1][0]
            target_tuple = item[1][1]
            predicate = seg[0][item[0]]
            content = ''.join(seg[0][content_tuple[1]:content_tuple[2]+1])
            target = ''.join(seg[0][target_tuple[1]:target_tuple[2]+1])

            content_label = self.create_content_txt(content)
            predicate_label = self.create_predicate_txt(predicate)
            target_num_tuple = self.get_number_tuple(target)
            return [(envir_label, content_label, predicate_label), target_num_tuple]


datactr = DataCtr()
# res = datactr.split_sentence('小明教小陈：中国的首都是北京。')
# res2 = datactr.split_sentence('小明教小陈：中国的首都有长城。')
# res3 = datactr.split_sentence('小明教小陈：中国的首都有故宫。')
# if res3:
#     neureCtr = getItem(str(res3[0][1]))
    # neureCtr.relevants = res3
    # smartUpDb(neureCtr)
    # print(neureCtr.relevants)
    # neureCtr.relevants = res
    # neureCtr.relevants = res2
    # smartUpDb(neureCtr)

res = datactr.split_sentence('小明教小陈：北京是中国的首都。')
res2 = datactr.split_sentence('小明教小陈：北京有长城。')
res3 = datactr.split_sentence('小明教小陈：北京有故宫。')
if res:
    neureCtr = getItem(str(res[0][1]))
    # neureCtr.relevants = res
    # neureCtr.relevants = res2
    # neureCtr.relevants =  res3
    # smartUpDb(neureCtr)
    relevants = neureCtr.relevants
    keys = list(relevants.keys())
    values = list(relevants.values())
    keys_words, values_words = [], []

    for i in range(len(keys)):
        envir_l, cont_l, pred_ = keys[i]
        keys_words.append((datactr.get_txt_from_label(envir_l, datactr.envir_labels_path), datactr.get_txt_from_label(cont_l, datactr.content_label_path), datactr.get_txt_from_label(pred_, datactr.predicate_label_path)))
        target = []
        for tuple_data in values[i]:
            target.append(datactr.get_txt_from_tuple(tuple_data))
        values_words.append(target)
    temp_dict = {}
    for i in range(len(keys)):
        temp_dict[keys_words[i]] = values_words[i]
    print(temp_dict)
