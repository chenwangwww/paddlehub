from ltp import LTP
ltp = LTP()

class Sentence(object):
    def __init__(self, sentence):
        self.dicA = {
            'zhuWord': None,
            'weiWord': None,
            'binWord': None,
        }
        self.arrZhuAttNoun = []
        self.arrInfo = []

        seg, hidden = ltp.seg([sentence])
        pos = ltp.pos(hidden)
        dep = ltp.dep(hidden)
        self.getArrInfo(seg, dep, pos)
        if len(self.arrInfo) > 0:
            hed = self.getHEDInfo(self.arrInfo)
            if hed is not None:
                sbv = self.getWordInfo(self.arrInfo, hed['dep'], 'SBV')
                vob = self.getWordInfo(self.arrInfo, hed['dep'], 'VOB')
                fob = self.getWordInfo(self.arrInfo, hed['dep'], 'FOB')
                
                self.dicA['zhuWord'] = zhuword = sbv
                self.dicA['weiWord'] = hed
                self.dicA['binWord'] = binword = vob or fob

                zhuword and self.getNounAttArr(self.arrInfo, zhuword['dep'], self.arrZhuAttNoun)
                for ser in self.arrInfo:
                    if ser['pos'] == 'n':
                        ser['num'] = self.getNumWord(ser['dep'])
                binword['num'] = self.getNumWord(binword['dep'])
                self.printInfo()

    #获取词的信息列表
    def getArrInfo(self, strArr, depArr, posArr):
        tempstrArr = strArr[0]
        tempstrArr.insert(0, "ROOT")
        tempposArr = posArr[0]
        tempposArr.insert(0, "ROOT")
        tempdepArr = depArr[0]

        tempArr = []
        for item in tempdepArr:
            dic = {
                "dep": tempstrArr[item[0]],
                "gov": tempstrArr[item[1]],
                "rel": item[2],
                "pos": tempposArr[item[0]],
                "num": None
            }
            tempArr.append(dic)
        self.arrInfo = tempArr

    #获取指定性质的词的信息
    def getWordInfo(self, words, GOV, wType, pos = None):
        sbv = None
        for word in words:
            if word['rel'] == wType and word['gov'] == GOV:
                if pos and pos in word['pos']:
                    sbv = word
                elif pos is None:
                    sbv = word
        return sbv

    #获取句子中的谓词信息
    def getHEDInfo(self, words):
        root = None
        for word in words:
            if word['gov'] == 'ROOT':
                root = word
        return root

    #获取数词
    def getNumWord(self, word):
        res = None
        w = self.getWordInfo(self.arrInfo, word, 'ATT', 'm')
        if w is not None:
            res = w['dep']
        else:
            w = self.getWordInfo(self.arrInfo, word, 'ATT', 'q')
            if w is not None:
                w2 = self.getWordInfo(self.arrInfo, w['dep'], 'ATT', 'm')
                if w2 is not None:
                    res = w2['dep']
        return res
    #获取定中关系的名词信息列表
    def getNounAttArr(self, words, word, resArr):
        w = self.getWordInfo(words, word, 'ATT', 'n')
        if w is not None:
            resArr.append(w)
            self.getNounAttArr(words, w['dep'], resArr)

    def printInfo(self):
        print(self.arrInfo)
        print('------------------')
        print(self.dicA)
        print('------------------')
        print(self.arrZhuAttNoun)

Sentence("三角形有三条边")