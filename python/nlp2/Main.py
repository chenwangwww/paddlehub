import sys
from Sentence import Sentence
from ClsTools import clsTools
from QuestionFilter import quesFilter

if __name__ == "__main__":
    strr = sys.argv[1]
    sentence = Sentence(strr)

    if quesFilter.bQues(strr):
        srlStr = clsTools.getData(sentence)
        print(srlStr)
    else:
        clsTools.setData(sentence)
    
    