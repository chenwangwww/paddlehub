import os

class FileFuncs(object):
    def __init__(self):
        pass

    #递归获取某一目录下的所有文件
    @classmethod
    def get_allFiles(self, cwd, result = []):
        get_dir = os.listdir(cwd)
        for i in get_dir:
            sub_dir = os.path.join(cwd, i)
            if os.path.isdir(sub_dir):
                FileFuncs.get_allFiles(sub_dir, result)
            else:
                result.append(i)

    #检查指定目录下是否存在指定名称和指定后缀名的文件
    @classmethod
    def hasTheFile(self, file, cwd, suffix):
        result = []
        FileFuncs.get_allFiles(cwd, result)
        for i in result:
            sp = i.split('.')
            if sp[0] == file and sp[1] == suffix:
                return True
        return False

    #检查指定目录下是否存在指定名称的python文件
    @classmethod
    def hasTheFilePY(self, file, cwd):
        return FileFuncs.hasTheFile(file, cwd, 'py')

class ClsTool(object):
    def __init__(self, sentInst):
        self._sentInst = sentInst

    #从句子的分词信息中提炼出类名和属性信息
    def get_cls_and_prop(self):
        arr = self._sentInst.arrZhuAttNoun
        length = len(arr)
        self.clsInfo = None if length == 0 else arr[0] if length == 1 else arr[-1]
        self.propInfo = None if length < 2 else arr[-2]       

    #获取句子中的类名
    def get_cls_in_sentence(self):
        result = None
        if len(self._sentInst.arrZhuAttNoun) > 0:
            result = self._sentInst.arrZhuAttNoun[-1]
        else:
            result = self._sentInst.dicA['zhuWord']
        return result

    #根据谓词判断该句子是翻译成定义、属性还是方法(1：定义；2：属性；3：方法)
    def makeSure_prop_or_method(self):
        result, weiword = None, self._sentInst.dicA['weiWord']
        if weiword == '是':
            result = 1
        elif weiword == '有':
            result = 2
        else:
            result = 3
        return result
  
    #创建类
    def dicToClass(self, cwd, zhuword):
        classStr = ''
        if zhuword is not None:
            classStr = "# -*- coding: UTF-8 -*-\n\n"
            classStr += "class " + (zhuword) + ":\n"
            classStr += "\tdef __init__(self):\n"
            classStr += "\n#this is __init__"
        if classStr != '':
            fo = open(cwd + "/" + zhuword + ".py", "w", encoding='utf-8')
            fo.write(classStr)
            fo.close()

    #检查是否存在指定类名的类
    def has_Cls_by_name(self, name, cwd):
        return FileFuncs.hasTheFilePY(name, cwd)

    #判断指定属性是否存在
    def has_prop_by_name(self, name, prop, cwd):
        fo = open(cwd + "/" + name + ".py", "r", encoding='utf-8')
        lines = fo.read()
        fo.close()
        index = lines.find("\n\t\tself.propsArr['" + prop + "'] = ")
        if index >= 0:
            return True
        else:
            return False

    #插入指定属性
    def insert_prop_info(self, name, prop, cwd, info):
        fo = open(cwd + "/" + name + ".py", "r", encoding='utf-8')
        lines = fo.read()
        fo.close()
        fo = open(cwd + "/" + name + ".py", "w", encoding='utf-8')
        hasProp = self.has_prop_by_name(name, prop, cwd)
        if hasProp:
            self.remove_prop(name, prop, cwd)

        index = lines.find("\n#this is __init__")
        if index >= 0:
            classStr = lines[:index]
            classStr += "\n\t\tself.propsArr['" + prop + "'] = "
            classStr += info
            classStr += lines[index:]
            fo.write(classStr)
        fo.close()

    #获取指定属性

    #删除指定属性
    def remove_prop(self, name, prop, cwd):
        fo = open(cwd + "/" + name + ".py", "r", encoding='utf-8')
        lines = fo.read()
        fo.close()
        fo = open(cwd + "/" + name + ".py", "w", encoding='utf-8')
        searchStr = "self.propsArr['" + prop + "'] = "
        arrLines = lines.split('\n')
        classStr = ''
        for linestr in arrLines:
            print(linestr)
            print(searchStr not in linestr)
            print('--------------')
            classStr += (linestr + '\n') if searchStr not in linestr else ''
        fo.write(classStr)
        fo.close()

    #判断是方法还是属性

    #判断指定方法是否存在

    #获取指定方法

    #插入指定方法

    #删除指定方法
    

# ClsTool('').remove_prop('三角形', '内角', 'python/nlp/dyCls')
ClsTool('').dicToClass('python/nlp/dyCls', '四边形')