import pickle
from InfoBase import InfoBase
from RuleBase import RuleBase
from QuesFliter import quesFliter
from DbCtr import ctr
from InfoCollector import infoCtr
from Responser import rpsr
import chardet
import sys
import pymysql
import Globals
from List import List

if __name__ == '__main__':
    #dic = {'from': '小明', 'to': '我', 'action': '说', 'content': '你吃饭了？'}
    item_ni = Globals.getDicInfoItem(str({'from': '小明', 'to': '我', 'action': '说', 'content': '你'}))
    item_ni.reflection = '我'
    Globals.smartUpDb(item_ni)

    item_chifan = Globals.RuleBase('吃饭')
    item_chifan.reflection = '吃午饭'
    Globals.smartUpDb(item_chifan)

    item = Globals.getDicInfoItem(str({'from': '小明', 'to': '我', 'action': '说', 'content': '你吃饭了？'}))
    item.cut = [
                    str({'from': '小明', 'to': '我', 'action': '说', 'content': '你'}),
                    '吃饭', '了', '？'
                ] 
    print(rpsr.getReflection(item))
    
    # ctr.truncateTb("tbnlp")

    #"a、b的和等于120"的数学表达式：a+b=120
    # item_a_b_he = Globals.getItem("a、b的和")
    # item_a_b_he.appendMeansItem("数学表达式:a+b")
    # Globals.smartUpDb(item_a_b_he)

    # item_dengyu = Globals.getItem("等于")
    # item_dengyu.appendMeansItem("数学表达式:=")
    # Globals.smartUpDb(item_dengyu)

    # item_120 = Globals.getItem("120")
    # item_120.appendMeansItem("数学表达式:120")
    # Globals.smartUpDb(item_120)

    # item = Globals.getItem("a、b的和等于120")
    # item.cut = ['a、b的和', '等于', '120']
    # print(rpsr.getMeanByKey(item, "数学表达式"))

    #“一加一等于二”的数学表达式：1+1=2
    # item_yi = Globals.getItem("一")
    # item_yi.appendMeansItem("数学表达式:1")
    # Globals.smartUpDb(item_yi)

    # item_jia = Globals.getItem("加")
    # item_jia.appendMeansItem("数学表达式:+")
    # Globals.smartUpDb(item_jia)

    # item_dengyu = Globals.getItem("等于")
    # item_dengyu.appendMeansItem("数学表达式:=")
    # Globals.smartUpDb(item_dengyu)

    # item_er = Globals.getItem("二")
    # item_er.appendMeansItem("数学表达式:2")
    # Globals.smartUpDb(item_er)

    # item = Globals.getItem("一加一等于二")
    # item.cut = ['一', '加', '一', '等于', '二']
    # Globals.smartUpDb(item)
    # print(rpsr.getMeanByKey(item, '数学表达式'))

    # print(type(list))
    # li = List()
    # li.append(10)
    # li.append('key:23')
    # ret = li.queryValByKey('key')
    # print(ret)

    # item = Globals.getRuleItem("两位数整数加法")
    # item.appendMeansItem("1+1=2")
    # item.appendMeansItem("1+2=3")
    # item.appendMeansItem("1+3=4")
    # item.appendMeansItem("1+4=5")
    # item.appendMeansItem("1+5=6")
    # item.appendMeansItem("1+6=7")
    # item.appendMeansItem("1+7=8")
    # item.appendMeansItem("1+8=9")
    # item.rule = ["个位+个位", "十位+十位"]

    # item1 = Globals.getItem("11")
    # item1.appendMeansItem("11是整数")
    # item1.appendMeansItem("个位是1")
    # item1.appendMeansItem("十位是1")

    # item2 = Globals.getItem("13")
    # item2.appendMeansItem("13是整数")
    # item2.appendMeansItem("个位是3")
    # item2.appendMeansItem("十位是1")

    # item3 = Globals.getItem("11+13=?")
    # item3.reflection = "两位数整数加法"
    # item3.cut = ['11', '13']
    

    # print(rpsr.bCorrect(infoCtr.info))

    # ctr.createTb(TBNAME)

    # item = Globals.getItem("我")
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

    # item1 = InfoBase(['1'], '1')
    # pic = pickle.dumps(item1)
    # d = pickle.loads(pic)
    # print(d.name)

    # item1 = InfoBase(['1'], '1')
    # item2 = InfoBase(['2'], '2')
    # itemPlus = InfoBase(['+'], '+')
    # itemPlus.appendMeansItem('加')
    # item3 = InfoBase(['1', '和', '1', '的', '和', '等于', '2'], '1和1的和等于2')
    # item3.appendMeansItem('1+1=2')
    # quesStr = '1+?=2'
    # quesTag = '?'
    # if quesFliter.bQues(quesStr):
    #     index = quesStr.find(quesTag)
    #     for mean in item3.means:
    #         if quesStr[:index] in mean and quesStr[index+len(quesTag):] in mean:
    #             print(mean)

#repr():字符串转原始字符串