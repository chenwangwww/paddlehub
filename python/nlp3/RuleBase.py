from InfoBase import InfoBase

class RuleBase(InfoBase):
    def __init__(self, name=None):
        super().__init__(name)
        self._rule = None

    @property
    def rule(self):
        return self._rule

    @rule.setter
    def rule(self,value):
        self._rule = value

    def useRule(self, cut):
        pass