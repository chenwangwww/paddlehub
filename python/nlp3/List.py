class List(list):
    def __init__(self):
        pass

    def queryValByKey(self, key):
        ret = None
        for item in self:
            itemArr = str(item).split(":")
            index = False if len(itemArr) <= 1 else itemArr[0] == key
            if index :
                ret = itemArr[1]
        return ret
