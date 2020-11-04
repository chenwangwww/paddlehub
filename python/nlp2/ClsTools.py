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
        zhuword = sentence.dicA['zhuWord']['dep']
        self.createTbl(tbName)
        arrInfo = self.queryData(tbName, weiword)
        print(arrInfo)
        # result = ''
        # for info in arrInfo:
        #     if zhuword in info:
        #         result = info
        #         break
        # return result

clsTools = ClsTools()

# ClsTools().createTbl("美国")
# ClsTools().insertData('美国', '是', '最富饶的地方')
# ClsTools().queryData('美国', '是')
# ClsTools().deleteTb('美国')