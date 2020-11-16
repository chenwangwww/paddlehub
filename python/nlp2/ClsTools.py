import sqlite3

def connDb(func):
    def para(self, *args, **kw):
        self.conn = sqlite3.connect('nlp2.db')
        self.cursor = self.conn.cursor()
        data = func(self, *args, **kw)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
        return data
    return para

class ClsTools(object):
    def __init__(self):
        self.conn = None
        self.cursor = None

    #创建数据表
    @connDb
    def createTbl(self, tbName):
        self.cursor.execute('create table if not exists ' + tbName + ' (id integer primary key autoincrement, weiword varchar(20), info varchar(255))')

    #插入数据
    @connDb
    def insertData(self, tbName, weiword, info):
        self.cursor.execute('insert into ' + tbName + ' (weiword, info) values (\'' + weiword + '\', \'' + info + '\')')

    #查询数据
    @connDb
    def queryData(self, tbName, weiword):
        self.cursor.execute('select * from ' + tbName + ' where weiword=?', (weiword, ))
        values = self.cursor.fetchall()
        return values

    #删除数据表
    @connDb
    def deleteTb(self, tbName):
        self.cursor.execute('drop table ' + tbName)

    def setData(self, sentence):
        tbName = sentence.arrZhuAttNoun[-1]['dep']
        weiword = sentence.dicA['weiWord']['dep']
        info = sentence.srlStr
        self.createTbl(tbName)
        self.insertData(tbName, weiword, info)

    def getData(self, sentence):
        tbName = sentence.arrZhuAttNoun[-1]['dep']
        weiword = sentence.dicA['weiWord']['dep']
        arrNoun = sentence.arrNoun
        self.createTbl(tbName)
        arrSrlStr = self.queryData(tbName, weiword)
        print(arrSrlStr)
        result = None
        for info in arrSrlStr:
            arr = list(filter(lambda val: val['dep'] in info[2], arrNoun))
            if len(arr) == len(arrNoun):
                result = info[2]
                break
        return result if result is None else self.srlToSent(result)

    #srlstr转成句子
    def srlToSent(self, srlStr):
        arrStr = srlStr.split('#')
        sentence = None 
        if len(arrStr) > 0:
            a0 = list(filter(lambda val: 'A0' in val, arrStr))[0]
            a1 = list(filter(lambda val: 'A1' in val, arrStr))[0]
            sentence = a0.split(':')[1] + arrStr[0] + a1.split(':')[1]
        return sentence

clsTools = ClsTools()

# ClsTools().createTbl("美国")
# ClsTools().insertData('美国', '是', '最富饶的地方')
# ClsTools().queryData('美国', '是')
# ClsTools().deleteTb('美国')