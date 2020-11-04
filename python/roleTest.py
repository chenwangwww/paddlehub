# -*- coding: UTF-8 -*-

# class triangle:
#     totalAngle = 180
#     def __init__(self):
#         pass

#     def getThirdAngle(self, angleA, angleB):
#         return triangle.totalAngle - angleA - angleB

# print(globals())
# a = triangle()
# b = triangle()
# print(a.getThirdAngle(30,60))
# print(b.getThirdAngle(60,90))

# fo = open("python/triangle.py", "w")
# strr = '''class triangle:
#     totalAngle = 180
#     def __init__(self):
#         pass

#     def getThirdAngle(self, angleA, angleB):
#         return triangle.totalAngle - angleA - angleB'''
# fo.write(strr)
# fo.close()

# import sys
# path = r'\\'.join(sys.path[0].split("\\")[:-1])
# sys.path.append(path)
# from triangle import triangle
# a = triangle()
# print(a.getThirdAngle(30,60))

# list = [11,22,343]
# l1,l2,l3 = list
# print(l3)

# def my_func(*args):
#     fs = []
#     j = 0
#     for i in range(3):
#         def func():
#             return j*j
#         fs.append(func)
#     j = 2
#     return fs

# fs1, fs2, fs3 = my_func()
# print(fs1())
# print(fs2())
# print(fs3())

# import pickle
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print("my name is {}, my age is {}".format(self.name, self.age))

# a = A('tom', 12)
# pickle.dump(a, open('./python/p.txt', 'wb'))

# a1 = pickle.load(open('./python/p.txt', 'rb'))
# a1.show()

import os

class File(object):
    result = []
    def __init__(self):
        pass

    #递归获取某一目录下的所有文件
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

# StudyTool.dicToClass({
#     'zhuWord': '三角形',    
#     'weiWord': '有',
#     'binWord': '内角',
#     'numbinWord': '3',
# })

# StudyTool.insertProp({
#     'zhuWord': '角度总和',    
#     'weiWord': '等于',
#     'binWord': '度',
#     'numbinWord': '180',
# }, '三角形')

# import sys
# path = sys.path[0] + "\\dynamicClasses"
# sys.path.append(path)
# from 三角形 import 三角形

# print(三角形().propsArr)

# str = "海湾战争的新动态"
# index = str.find("的")
# classStr = str[:index-2]
# subStr = str[index:]
# print(index)
# print(classStr)
# print(subStr)

# File.get_allFiles('python/dynamicClasses')
# print(File.result)
# re = StudyTool.searchCls([{'dep':'内角'}, {'dep':'三角形'}])
# print(re)

# a, b =100, 300
# print(a,b)

# a = 'dd' or None
# print(a)

# a = set((1,2,3))
# a.add((1,2))
# print(a)

# class Student(object):
#     __slots__ = ('name', 'age')
#     def __init__(self):
#         self.age = 99

# import jieba.posseg as pseg
# words = pseg.cut("好漂亮的彩虹啊！")
# for word, flag in words:
#     print('%s %s' % (word, flag))