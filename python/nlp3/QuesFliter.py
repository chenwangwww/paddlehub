class QuesFliter:
    def __init__(self):
        self._kws = ['?']

    def bQues(self, sentence):
        for item in self._kws:
            if item in sentence:
                return True
        return False
quesFliter = QuesFliter()