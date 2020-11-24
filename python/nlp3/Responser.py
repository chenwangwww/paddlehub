from BaseCls import BaseCls
import Globals

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

    #判断信息是好的，还是坏的

rpsr = Responser()