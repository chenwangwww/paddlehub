import pickle
from BaseCls import BaseCls
from QuesFliter import quesFliter
from DbCtr import ctr
from InfoCollector import infoCtr
from Responser import rpsr
import chardet
import sys
import pymysql
import Globals

if __name__ == '__main__':
    print(rpsr.bCorrect(infoCtr.info))

    # ctr.createTb(TBNAME)

    item = Globals.getItem("我")
    # item.appendMeansItem('我就是小王')
    # item.appendMeansItem('我是人')
    # item.reflection = "我"
    # ctr.insertData(TBNAME, {'name':item.name, 'sequence':pickle.dumps(item)})

    # item = getItem("对")
    # print(item.means)
    # print(item.reflection)
    # item.appendMeansItem('小明是个人')
    # item.appendMeansItem('小王就是我')
    # item.reflection = "对"
    # ctr.updateData(TBNAME, item.name, pickle.dumps(item))
    # ctr.insertData(TBNAME, {'name':item.name, 'sequence':pickle.dumps(item)})

    # ctr.truncateTb(TBNAME)
    # ctr.createTb(TBNAME)
    # item = getItem('1')
    # print(item.means)
    # bytes('123', 'utf-8')
    # a = len(bytes('123', 'utf-8'))
    # s = pymysql.Binary(pickle.dumps(item))
    # print(sys.getsizeof(s))
    # item.appendMeansItem('1是一个阿拉伯数字')
    # item.appendMeansItem('1是一个自然数')
    # item.appendMeansItem('1是最小的正整数')
    # ctr.updateData(TBNAME, item.name, pickle.dumps(item))
    # ctr.insertData(TBNAME, {'name':item.name, 'sequence':pickle.dumps(item)})

    # item1 = BaseCls(['1'], '1')
    # pic = pickle.dumps(item1)
    # d = pickle.loads(pic)
    # print(d.name)

    # item1 = BaseCls(['1'], '1')
    # item2 = BaseCls(['2'], '2')
    # itemPlus = BaseCls(['+'], '+')
    # itemPlus.appendMeansItem('加')
    # item3 = BaseCls(['1', '和', '1', '的', '和', '等于', '2'], '1和1的和等于2')
    # item3.appendMeansItem('1+1=2')
    # quesStr = '1+?=2'
    # quesTag = '?'
    # if quesFliter.bQues(quesStr):
    #     index = quesStr.find(quesTag)
    #     for mean in item3.means:
    #         if quesStr[:index] in mean and quesStr[index+len(quesTag):] in mean:
    #             print(mean)

#repr():字符串转原始字符串