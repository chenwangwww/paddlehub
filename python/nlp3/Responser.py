from enum import Enum
from List import List
import Globals

class Emotion(Enum):
    LOVE = 1
    ANGRY = 2
    SAD = 3
    HAPPY = 4

class Responser(object):
    def __init__(self):
        pass

    #判断信息是否正确
    def bCorrect(self, info):
        content = info['content']
        to = info['to']
        toItem = Globals.getItem(to)
        print(toItem.means)
        print(content)
        return True if content in toItem.means else False

    #根据信息来产生情绪
    def generateEmotion(self, info):
        return Emotion.ANGRY

    #根据键名获取相应的含义
    def getMeanByKey(self, item, key):
        ret = None
        retArr = []
        if key is not None:
            for val in item.cut:
                it = Globals.getItem(val)
                rett = it.means.queryValByKey(key)
                if rett is not None:
                    retArr.append(rett)
            ret = None if len(retArr) == 0 else ' '.join(retArr)
        return ret

    #获取信息反射
    def getReflection(self, item):
        ret = None
        retArr = []
        for val in item.cut:
            it = Globals.getDicInfoItem(val)
            ref = it.reflection
            print(ref)
            if ref is not None:
                retArr.append(ref)
        ret = None if len(retArr) == 0 else ' '.join(retArr)
        return ret

rpsr = Responser()