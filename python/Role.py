# -*- coding: UTF-8 -*-
import os
from ltp import LTP
ltp = LTP()
ltp.init_dict(path="words.txt", max_window=3)

class File(object):
    result = []
    def __init__(self):
        pass

    @classmethod
    def get_realAllFiles(self, cwd):
        get_dir = os.listdir(cwd)
        for i in get_dir:
            sub_dir = os.path.join(cwd, i)
            if os.path.isdir(sub_dir):
                File.get_realAllFiles(sub_dir)
            else:
                File.result.append(i)

    @classmethod
    def get_allFiles(self, cwd):
        File.result = []
        File.get_realAllFiles(cwd)

    @classmethod
    def hasTheFile(self, file):
        for i in File.result:
            sp = i.split('.')
            if sp[0] == file and sp[1] == 'py':
                return True
        return False

class StudyTool(object):
    def __init__(self):
        pass

    @staticmethod
    def writeProp(dicA):
        subStr = ''
        if dicA['weiWord'] == '有':
            if dicA['numbinWord'] is not None:
                if int(dicA['numbinWord']) == 0:
                    subStr += "[]"
                else:
                    subStr += "[None"
                    for i in range(int(dicA['numbinWord'])-1):
                        subStr += ", None"
                    subStr += "]"
        elif dicA['weiWord'] == '等于':
            subStr += dicA['numbinWord']
        return subStr
        

    @staticmethod
    def dicToClass(dicA):
        classStr = ''
        if dicA['zhuWord'] is not None:
            classStr = "# -*- coding: UTF-8 -*-\n\n"
            classStr += "class " + (dicA['zhuWord']) + ":\n"
            classStr += "\tpropsArr = { }\n"
            if dicA['binWord'] is not None:
                classStr += "\tdef __init__(self):\n"
                classStr += "\t\tself.propsArr['" + dicA['binWord'] + "'] = "
                classStr += StudyTool.writeProp(dicA)
                classStr += "\n#this is __init__\n"
        if classStr != '':
            fo = open("python/dynamicClasses/" + dicA['zhuWord'] + ".py", "w", encoding='utf-8')
            fo.write(classStr)
            fo.close()

    @staticmethod
    def searchCls(words):
        for wordinfo in words:
            clsName = wordinfo['dep']
            if File.hasTheFile(clsName):
                return clsName
        return None

    @staticmethod
    def insertProp(dicA, clsName):
        fo = open("python/dynamicClasses/" + clsName + ".py", "r", encoding='utf-8')
        lines = fo.read()
        fo.close()
        fo = open("python/dynamicClasses/" + clsName + ".py", "w", encoding='utf-8')
        index = lines.find("\n#this is __init__")
        if index >= 0:
            classStr = lines[:index]
            if dicA['zhuWord'] is not None:
                classStr += "\n\t\tself.propsArr['" + dicA['zhuWord'] + "'] = "
                classStr += StudyTool.writeProp(dicA)
            classStr += lines[index:]
            fo.write(classStr)
        fo.close()

class Sentence(object):
    dicA = {             
        'zhuWord': '',    
        'weiWord': '',
        'binWord': '',
        'numbinWord': '',
    }
    def __init__(self):
        pass

    @classmethod
    def trans2Result(self, strArr, depArr, posArr):
        tempstrArr = strArr[0]
        tempstrArr.insert(0, "ROOT")
        tempposArr = posArr[0]
        tempposArr.insert(0, "ROOT")
        tempdepArr = depArr[0]
        
        tempArr = []
        for item in tempdepArr:
            dic = {
                "dep": tempstrArr[item[0]],
                "gov": tempstrArr[item[1]],
                "aa": item[2],
                "pos": tempposArr[item[0]]
            }
            tempArr.append(dic)
        return tempArr

    @classmethod
    def getHED(self, words):
        root = None
        for word in words:
            if word['gov'] == 'ROOT':
                root = word['dep']
        return root

    @classmethod
    def getWord(self, words, HED, wType):
        sbv = None
        for word in words:
            if word['aa'] == wType and word['gov'] == HED:
                sbv = word['dep']
        return sbv

    @classmethod
    def getWordInfo(self, words, HED, wType):
        sbv = None
        for word in words:
            if word['aa'] == wType and word['gov'] == HED:
                sbv = word
        return sbv

    @classmethod
    def getWordInfoContainT(self, words, HED, wType, wordT):
        sbv = None
        for word in words:
            if word['aa'] == wType and word['gov'] == HED and word['pos'][0] == wordT:
                sbv = word
        return sbv

    @classmethod
    def getFirstNotNone(self, array):
        for word in array:
            if word is not None:
                return word
        return None

    @classmethod
    def getNumbin(self, array1, array2):
        for word in array1:
            if word is not None:
                w = Sentence.getWordInfo(array2, word, 'ATT')
                if w is None:
                    break
                if w['pos'] == 'm':
                    return w['dep']
                else:
                    w2 = Sentence.getWordInfo(array2, w['dep'], 'ATT')
                    if w2 is not None and w2['pos'] == 'm':
                        return w2['dep']
        return None

    @classmethod
    def getAttArr(self, array, word, wordT, resArr):
        w = Sentence.getWordInfoContainT(array, word, 'ATT', wordT)
        if w is not None :
            resArr.append(w)
            Sentence.getAttArr(array, w['dep'], wordT, resArr)

    @classmethod
    def abstractSentence(self, sentence):
        seg, hidden = ltp.seg([sentence])
        dep = ltp.dep(hidden)               #依存句法分析
        pos = ltp.pos(hidden)               #词性标注
        
        array = Sentence.trans2Result(seg, dep, pos)
        print(array)
        
        if len(array) > 0:
            hed = Sentence.getHED(array)
            if hed is not None:
                sbv = Sentence.getWord(array, hed, 'SBV')
                vob = Sentence.getWord(array, hed, 'VOB')
                fob = Sentence.getWord(array, hed, 'FOB')
                adv = Sentence.getWord(array, hed, 'ADV')
                pob = Sentence.getWord(array, adv, 'POB')

                zhuWord = Sentence.getFirstNotNone([sbv, pob])
                weiWord = hed
                binWord = Sentence.getFirstNotNone([vob, fob, pob])
                numbinWord = Sentence.getNumbin([vob, fob, pob], array)

                Sentence.dicA = {             
                    'zhuWord': zhuWord,    
                    'weiWord': weiWord,
                    'binWord': binWord,
                    'numbinWord': numbinWord,
                }

                resArr = []
                Sentence.getAttArr(array, zhuWord, 'n', resArr)
                print(resArr)
                # print(numbinWord)
                result = '{}{}{}{}'.format(zhuWord, weiWord, numbinWord, binWord)
        return Sentence.dicA

class Role(object):
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            print("error: 输入类型与预设类型不一致")

    def abstractSentence(self, value):
        return Sentence.abstractSentence(value)

role = Role()
print(role.abstractSentence("三角形三个内角的和等于180度。"))

seg, hidden = ltp.seg(["三角形三个内角的和等于180度。"])
dep = ltp.dep(hidden)                           #依存句法分析
pos = ltp.pos(hidden)                           #词性标注
sdp = ltp.sdp(hidden)                           #语义依存分析
srl = ltp.srl(hidden, keep_empty=False)         #语义角色标注
print(seg)
print(pos)
print(sdp)
print(srl)
print(dep)

# sents = ltp.sent_split(["已知三角形2个内角的角度和.最后一个内角的角度等于180减去这2个内角的角度和"])
# print(sents)

# "三角形1个内角的角度等于180减去另2个内角的角度"
# "三角形有3个内角。"
# "三角形有3条边。"
# "锐角三角形"
# "三角形的三个内角都小于90度。"
# "三角形的三个内角中有一个角大于90度。"
# "钝角三角形：三角形的三个内角中最大角大于90度，小于180度。"
# "三条边都不相等的三角形叫不等边三角形。"
# "三角形的内角和等于180°"
# "一个三角形的三个内角中最少有两个锐角"