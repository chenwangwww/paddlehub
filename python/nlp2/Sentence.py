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
        self.srlStr = ''

        seg, hidden = ltp.seg([sentence])
        pos = ltp.pos(hidden)
        dep = ltp.dep(hidden)
        srl = ltp.srl(hidden, keep_empty=False)
        print(seg)
        print(pos)
        print(srl)
        
        #先setSRLInfo，再getArrInfo，顺序不能调换
        self.setSRLInfo(seg, srl)
        self.getArrInfo(seg, dep, pos)
        if len(self.arrInfo) > 0:
            hed = self.getHEDInfo(self.arrInfo)
            if hed is not None:
                sbv = self.getWordInfo(self.arrInfo, hed['dep'], 'SBV')
                vob = self.getWordInfo(self.arrInfo, hed['dep'], 'VOB')
                fob = self.getWordInfo(self.arrInfo, hed['dep'], 'FOB')
                
                self.dicA['zhuWord'] = zhuword = sbv
                self.dicA['weiWord'] = hed
                self.dicA['binWord'] =vob or fob

                zhuword and self.arrZhuAttNoun.append(zhuword)
                zhuword and self.getNounAttArr(self.arrInfo, zhuword['dep'], self.arrZhuAttNoun)

                # self.printInfo()

    def setSRLInfo(self, seg, srl):
        temp = srl[0][0][1]
        resStr = seg[0][srl[0][0][0]] + '#'
        for item in temp:
            resStr += (item[0] + ':' + ''.join(seg[0][item[1]:item[2]+1]) + '#')
        self.srlStr = resStr
    
    def getArrInfo(self, strArr, depArr, posArr):
        tempstrArr = strArr[0]
        tempstrArr.insert(0, 'ROOT')
        tempposArr = posArr[0]
        tempposArr.insert(0, 'ROOT')
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

    def getWordInfo(self, words, GOV, wType, pos = None):
        sbv = None
        for word in words:
            if word['rel'] == wType and word['gov'] == GOV:
                if pos and pos in word['pos']:
                    sbv = word
                elif pos is None:
                    sbv = word
        return sbv

    def getHEDInfo(self, words):
        root = None
        for word in words:
            if word['gov'] == 'ROOT':
                root = word
        return root

    def getNounAttArr(self, words, GOV, resArr):
        w = self.getWordInfo(words, GOV, 'ATT', 'n')
        if w is not None:
            resArr.append(w)
            self.getNounAttArr(words, w['dep'], resArr)

    def printInfo(self):
        print(self.arrInfo)
        print('------------------')
        print(self.dicA)
        print('------------------')
        print(self.arrZhuAttNoun)
        print('------------------')
        print(self.srlStr)

