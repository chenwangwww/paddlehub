#1+1=2， 1和1的和等于2
#小明对小王说：“你是头猪。”，小王先产生反射：“我是头猪，猪是贬义词。”，小王后产生反应：“你（指小明）才是头猪。”。
# {'from': '小明', 'to': '我', 'action': '说', 'content': '猪'}

class BaseCls(object):
    def __init__(self, cut = [], name = None):
        self._means = []
        self._means.append(name)
        self._cut = cut
        self._name = name
        self._reflection = ''       #反射
        self._response = ''         #反应


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
    
    # def getReflection(self, sentence):
        # self._reflection = '小明对我说：“我就是头猪”，猪是肮脏，难看的东西。'

    def getResponse(self):
        #先进行比较，我是人，而不是猪，通过self._reflection，这是一句贬义词。
        self._response = '我对小明说：“你才是一头猪。”'
