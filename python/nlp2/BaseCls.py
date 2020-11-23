#1+1=2， 1和1的和等于2

class BaseCls(object):
    def __init__(self, cut = [], name = None):
        self._mean = []
        self._mean.append(name)
        self._cut = cut
        self._name = name

    @property
    def cut(self):
        return self._cut

    @cut.setter
    def cut(self, value):
        if value is not None and isinstance(value, list):
            self._cut = value
        
    @property
    def mean(self):
        return self._mean

    def appendMeanItem(self, value):
        self._mean.append(value)

    @property
    def name(self):
        return self._name

item1 = BaseCls(['1'], '1')
item2 = BaseCls(['2'], '2')
item3 = BaseCls(['1', '和', '1', '的', '和', '等于', '2'], '1和1的和等于2')
item3.appendMeanItem('1+1=2')