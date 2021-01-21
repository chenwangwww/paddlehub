import pickle
from DbCtr import ctr
from InfoBase import InfoBase
from RuleBase import RuleBase
from DicInfoBase import DicInfoBase
from Functions import getMd5

TBNAME = "tbnlp"

def getItem(name, type = "infobase"):
    item = None
    md5 = getMd5(name)
    query = ctr.queryData(TBNAME, md5)
    if query:
        item = pickle.loads(query[1])
    else:
        if type == "infobase":
            item = InfoBase(name=name)
        elif type == "rulebase":
            item = RuleBase(name=name)
        elif type == "dicinfobase":
            item = DicInfoBase(name=name)
    return item

def getRuleItem(name):
    return getItem(name, "rulebase")

def getDicInfoItem(name):
    return getItem(name, "dicinfobase")

def smartUpDb(item):
    query = ctr.queryData(TBNAME, item.md5)
    if query:
        ctr.updateData(TBNAME, item.md5, pickle.dumps(item))
    else:
        ctr.insertData(TBNAME, {'name':item.md5, 'sequence':pickle.dumps(item)})