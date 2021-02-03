from sklearn.svm import SVC
import numpy as np
from ltp import LTP
ltp = LTP()
svc = SVC(kernel='linear')

class NeureCtr:
    def __init__(self, id):
        self._uuid = id
        self._relevants = {}

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

class dataCtr:
    def __init__(self):
        self.dict_path = 'dict_txt.txt'
        self.dict_num_path = 'dict_num_txt.txt'
        self.names_path = 'names.txt'
        self.actions_path = 'actions.txt'
        self.environment_label_path = 'envir_labels.txt'
        self.content_label_path = 'content_labels.txt'
        self.target_label_path = 'target_label.txt'
        self.predicate_path = 'predicate_label.txt'
        self.dict_labels_path = 'dict_labels.txt'
        self.create_dict()
        self.fitData_linear()

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
    
    def create_dict(self):
        self.dict_txt = self.get_dict_txt(self.dict_path)
        self.dict_num_txt = self.get_dict_txt(self.dict_num_path)

    def insert_txt(self, txt):
        txt_temp = ''
        keys = self.dict_txt.keys()
        for s in txt:
            if s not in keys:
                txt_temp += s
        count = len(keys)
        for s in txt_temp:
            self.dict_txt[s] = count
            self.dict_num_txt[count] = s
            count += 1
        with open(self.dict_path, 'w', encoding='utf-8') as f:
            f.write(str(self.dict_txt))
        with open(self.dict_num_path, 'w', encoding='utf-8') as f:
            f.write(str(self.dict_num_txt))

    #从汉字-数字对照表dict_txt.txt中获取数字元组
    def get_number_tuple(self, text):
        list_data = []
        for s in text:
            list_data.append(self.dict_txt[s])
        return tuple(list_data)

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
        with open(self.environment_label_path, 'w', encoding='utf-8') as f:
            f.write(str(dict(list_envir)))

    def create_content_txt(self, content):
        return self.create_dict_txt(content, self.content_label_path)

    def create_target_txt(self, target):
        return self.create_dict_txt(target, self.target_label_path)

    def create_predicate_txt(self, predicate):
        return self.create_dict_txt(predicate, self.predicate_path)

    def create_dict_txt(self, text, path):
        lines = self.get_dict_txt(path)
        self.insert_txt(text)        
        tuple_data = self.get_number_tuple(text)
        if tuple_data not in lines:
            lines.update({tuple_data: len(lines)})
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(lines))
        return lines[tuple_data]

    def split_sentence_ltp(self, sentence):
        seg, hidden = ltp.seg([sentence])
        pos = ltp.pos(hidden)
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
            target_label = self.create_target_txt(target)
            
            return {'content_label':content_label, 'predicate_label':predicate_label, 'target_label':target_label}

    def split_sentence_out(self, content, bteach):
        arr = [val.strip() for val in content.split("：")]
        if len(arr) != 2:
            return

        res = self.split_sentence_ltp(arr[1])
        if res:
            self.insert_txt(arr[0])        
            tuple_data = self.get_number_tuple(arr[0])
            envir_labels = self.get_dict_txt(self.environment_label_path)
            if len(envir_labels) > 0:
                res.update({'envir_label':envir_labels[tuple_data]})
                labels = self.get_list_txt(self.dict_labels_path)
                if res not in labels:
                    labels.append(res)
                    if bteach:
                        self.set_txt(self.dict_labels_path, labels)
                return res

    #将字符串写入文本
    def set_txt(self, path, content):
        with open(path, 'w', encoding='utf-8') as f:                    
            f.write(str(content))

    #线性分类训练数据
    def fitData_linear(self):
        lines = self.get_list_txt(self.dict_labels_path)
        data, target = [], []
        for item in lines:
            data.append([item['envir_label'], item['content_label'], item['predicate_label']])
            target.append(item['target_label'])
        svc.fit(data, target)

    #文字转标签字典
    def words_to_labels(self, item):
        data = [[item['envir_label'], item['content_label'], item['predicate_label']]]
        predict = svc.predict(data)
        if len(predict) > 0:
            lines = self.get_dict_txt(self.target_label_path)
            predict_tuple = list(filter(lambda k:lines[k]==predict, lines))[0]
            strr = ''
            for s in predict_tuple:
                strr += self.dict_num_txt[s]
            print(strr)

    def action_func(self, content, bteach = False):
        item = self.split_sentence_out(content, bteach)
        if not bteach:
            self.words_to_labels(item)

ctr = dataCtr()
# ctr.insert_txt('小明问：陈望，你几岁了？')
# ctr.create_environment_txt()

#小明教小陈：中国的首都是北京。
#小明问小陈：中国的首都是哪里？
#小明教小陈：北京的景区有长城。
#小明问小陈：北京的景区有哪些？
# ctr.create_content_txt('中国的首都')
# print(ctr.split_sentence_ltp('北京'))
# ctr.split_sentence_out('小明说小陈：北京有长城。')
# ctr.split_sentence_out('小明教小陈：中国的首都是北京。')
# ctr.fitData_linear()
# ctr.words_to_labels('小明教小陈：中国的首都是北京。')
# ctr.action_func('小明问小陈：北京的景区有哪些？')