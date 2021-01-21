from Functions import getMd5
from List import List
#1+1=2， 1和1的和等于2
#小明对小王说：“你是头猪。”，小王先产生反射：“我是头猪，猪是贬义词。”，小王后产生反应：“你（指小明）才是头猪。”。
# {'from': '小明', 'to': '我', 'action': '说', 'content': '猪'}

class InfoBase(object):
    def __init__(self, name = None):
        self._means = List()
        self._means.append(name)
        self._cut = []
        self._name = name
        self._md5 = getMd5(name)
        self._reflection = None       #反射

    @property
    def cut(self):
        return self._cut

    @cut.setter
    def cut(self, value):
        if value is not None and isinstance(value, list):
            self._cut = value
        
    @property
    def means(self):
        return self._means

    def appendMeansItem(self, value):
        self._means.append(value)

    @property
    def name(self):
        return self._name

    @property
    def reflection(self):
        return self._reflection

    @reflection.setter
    def reflection(self, value):
        self._reflection = value
    
    @property
    def md5(self):
        return self._md5

    @md5.setter
    def md5(self, value):
        self._md5 = value