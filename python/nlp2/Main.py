from Sentence import Sentence
from ClsTools import clsTools

if __name__ == "__main__":
    sentence = Sentence("政府鼓励个人投资服务业。")
    clsTools.setData(sentence)
    clsTools.getData(sentence)
