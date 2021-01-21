from InfoBase import InfoBase
class childCls(InfoBase):
    def test(self):
        pass
    def __init__(self):
        super().__init__()
        print("child")

childCls()