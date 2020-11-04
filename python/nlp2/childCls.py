from BaseCls import BaseCls
class childCls(BaseCls):
    def test(self):
        pass
    def __init__(self):
        super().__init__()
        print("child")

childCls()