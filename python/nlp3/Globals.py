import pickle
from DbCtr import ctr
from BaseCls import BaseCls

TBNAME = "tbNlp"

def getItem(name):
    item = None
    query = ctr.queryData(TBNAME, name)
    if query:
        item = pickle.loads(query[1])
    else:
        item = BaseCls(name=name)
    return item