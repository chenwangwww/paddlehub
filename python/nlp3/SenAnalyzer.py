class SenAnalyzer:
    def __init__(self):
        pass

    def analyse(self, sentence):
        length = len(sentence)
        if length == 1:
            #搜索这个词的_means列表
            pass
        elif length > 1:
            #先确定分析的顺序，再顺序搜索每个词的_means列表
            pass