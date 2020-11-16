class QuestionFilter(object):
    def __init__(self):
        self.quesKeys = ['哪里', '什么', '几个', '几条']

    #判断是否是疑问句
    def bQues(self, sentence):
        lister = list(filter(lambda val: val in sentence, self.quesKeys))
        return len(lister) != 0

quesFilter = QuestionFilter()