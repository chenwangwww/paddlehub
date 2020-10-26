import os

class FileFunctions(object):
    def __init__(self):
        pass

    #递归获取某一目录下的所有文件
    @classmethod
    def get_allFiles(self, cwd, result = []):
        get_dir = os.listdir(cwd)
        for i in get_dir:
            sub_dir = os.path.join(cwd, i)
            if os.path.isdir(sub_dir):
                FileFunctions.get_allFiles(sub_dir, result)
            else:
                result.append(i)

    #检查指定目录下是否存在指定名称和指定后缀名的文件
    @classmethod
    def hasTheFile(self, file, cwd, suffix):
        result = []
        FileFunctions.get_allFiles(cwd, result)
        for i in result:
            sp = i.split('.')
            if sp[0] == file and sp[1] == suffix:
                return True
        return False

    #检查指定目录下是否存在指定名称的python文件
    @classmethod
    def hasTheFilePY(self, file, cwd):
        return FileFunctions.hasTheFile(file, cwd, 'py')

class ClsTool(object):
    def __init__(self, sentInst):
        self._sentInst = sentInst

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

    #检查是否存在相关类

    #搜索类

    #判断指定属性是否存在

    #获取指定属性

    #插入指定属性

    #删除指定属性

    #判断是方法还是属性

    #判断指定方法是否存在

    #获取指定方法

    #插入指定方法

    #删除指定方法
    