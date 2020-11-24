#从环境中收集信息
class InfoCollector(object):
    def __init__(self):
        self._info = {'from': '小明', 'to': '我', 'action': '说', 'content': '我是人'}

    @property
    def info(self):
        return self._info

infoCtr = InfoCollector()