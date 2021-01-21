import os
from sklearn.svm import SVC
import numpy as np

class CodeTuple(object):
    def __init__(self, dict_path):
        with open(dict_path, 'r', encoding='utf-8') as f:
            self.dict_txt = eval(f.readlines()[0])
        self.keys = self.dict_txt.keys()
    def strToCodeTuple(self, content):
        dict_temp = []
        for s in content:
            if s in self.keys:
                dict_temp.append(self.dict_txt[s])
        return tuple(dict_temp)

codeTuple = CodeTuple('./python/sklearn_study/talk_txt.txt')
svc = SVC(kernel='linear')

def create_dict(data_path, dict_path, dict_num_path):
    dict_set = set()
    with open(data_path, 'r', encoding='utf-8') as f:       
        lines = f.readlines()
    for line in lines:
        title = line.split(':')[-1].strip()
        for s in title:
            dict_set.add(s)
    dict_list = []
    dict_list_num = []
    i = 0
    for s in dict_set:
        dict_list.append([s,i])
        dict_list_num.append([i,s])
        i+=1
    dict_txt = dict(dict_list)
    dict_txt_num = dict(dict_list_num)
    with open(dict_path, 'w', encoding='utf-8') as f:
        f.write(str(dict_txt))
    with open(dict_num_path, 'w', encoding='utf-8') as f:
        f.write(str(dict_txt_num))

# create_dict('./python/sklearn_study/talk.txt', './python/sklearn_study/talk_txt.txt', './python/sklearn_study/talk_num.txt')

def create_rule_dict(data_path, dict_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    from_set = set()
    for line in lines:
        from_set.add(line.split(':')[0])
    data_list = []
    i = 0
    for line in lines:
        arr = line.split(':')
        arr[1] = arr[1].strip()
        from_ = arr[0]
        wensign = arr[1].find("？")
        targets = list(filter(lambda val: val > -1, map(lambda val: arr[1].find(val + '，'), from_set)))
        if wensign > -1:
            if len(targets) == 1:
                to_ = arr[1][list(targets)[0]]
            else:
                to_ = 'all'
        else:
            to_ = None
        data_list.append([i, {
            'from':from_,
            'to':to_,
            'content':arr[1]
        }])
        i += 1
    with open(dict_path, 'w', encoding='utf-8') as f:
        f.write(str(dict(data_list)))

# create_rule_dict('./python/sklearn_study/talk.txt', './python/sklearn_study/talk_data.txt')

def create_feature_viron_dict(data_path, data_feature_environment_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    dict_set = set()
    for line in lines:
        dict_set.add(line.split(':')[0])
    dict_set.add(None)
    dict_set.add('all')
    dict_list = []
    i = 0
    for item in dict_set:
        for item2 in dict_set:
            if item and item != 'all' and item != item2:
                dict_list.append([item + '-' + str(item2), i])
                i += 1
    dict_txt = dict(dict_list)
    with open(data_feature_environment_path, 'w', encoding='utf-8') as f:
        f.write(str(dict_txt))
    

# create_feature_viron_dict('./python/sklearn_study/talk.txt', './python/sklearn_study/talk_feature_envir.txt')

def create_feature_content_dict(data_path, feature_content_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    dict_num = []
    i = 0   
    for line in lines:
        content = line.split(':')[-1].strip()    
        dict_num.append([codeTuple.strToCodeTuple(content), i])
        i += 1
    with open(feature_content_path, 'w', encoding='utf-8') as f:
        f.write(str(dict(dict_num)))

# create_feature_content_dict('./python/sklearn_study/talk.txt', './python/sklearn_study/talk_feature_content.txt')

def create_label_dict(data_data_path, label_path, envir_path, content_path):
    with open(data_data_path, 'r', encoding='utf-8') as f:
        dict_data = eval(f.readlines()[0])
    with open(envir_path, 'r', encoding='utf-8') as f:
        dict_envir = eval(f.readlines()[0])
    with open(content_path, 'r', encoding='utf-8') as f:
        dict_content = eval(f.readlines()[0])
    length = len(dict_data)
    list_label = []
    for i in range(length):
        item = dict_data[i]
        envir_label = dict_envir[item['from'] + '-' + str(item['to'])]
        content_label = dict_content[codeTuple.strToCodeTuple(item['content'])]
        if item['to'] == None:
            pass
        elif item['to'] == 'all':
            list_label.append({
                'data':(envir_label, content_label),
                'quesr':i,
                'asker':(i+1, i+2),
                'target':i,
            })
        else:
            list_label.append({
                'data':(envir_label, content_label),
                'quesr':i,
                'asker':(i+1,),
                'target':i,
            })
    with open(label_path, 'w', encoding='utf-8') as f:
        f.write(str(list_label))

# create_label_dict('./python/sklearn_study/talk_data.txt', './python/sklearn_study/talk_label.txt', './python/sklearn_study/talk_feature_envir.txt', './python/sklearn_study/talk_feature_content.txt')

def fitData(label_path):
    with open(label_path, 'r', encoding='utf-8') as f:
        dict_label = eval(f.readlines()[0])
    data, target = [], []
    for item in dict_label:
        data.append(list(item['data']))
        target.append(item['target'])
    data, target = np.array(data), np.array(target)
    
    svc.fit(data, target)

    print(target)
    predict = svc.predict(data)
    print(predict)


# fitData('./python/sklearn_study/talk_label.txt')

def targetToAnswer(target, label_path, data_path):
    with open(label_path, 'r', encoding='utf-8') as f:
        dict_label = eval(f.readlines()[0])
    with open(data_path, 'r', encoding='utf-8') as f:
        dict_data = eval(f.readlines()[0])
    item = filter(lambda val: val['target'] == target, dict_label)
    asker = list(item)[0]['asker']
    print(asker)
    for val in asker:
        print(dict_data[val])
    

targetToAnswer(5, './python/sklearn_study/talk_label.txt', './python/sklearn_study/talk_data.txt')