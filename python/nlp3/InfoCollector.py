#从环境中收集信息
class InfoCollector(object):
    def __init__(self):
        self._info = None #{'from': '小明', 'to': '我', 'action': '说', 'content': '你是猪'}

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

infoCtr = InfoCollector()

#{'from': '老师', 'to': '我', 'action': '问', 'content': '12+34=?'}
#  反射成   {'from': '德高望重的老师', 'to': '我', 'action': '问', 'content': '12+34=?，这是一道数学题。'}
#深度学习   回答
#反应过程   这是一道数学题 => 
#               根据 ‘+’ 号，这是一道加法题，加数分别是12、34，两个整数 => 
#               根据整数加法法则：从低位加起，满10进1（个位相加，满10进一，十位相加，满10进一）。12，1是高位，2是低位，34，3是高位，4是低位。=>
#               1+3=4，2+4=6. =>
#               46
#  反应成   {'from': '我', 'to': '老师', 'action': '回答', 'content': '12+34=46'}

#{'from': '老师', 'to': '我', 'action': '问', 'content': '1+1=?'}
#  反射成   {'from': '德高望重的老师', 'to': '我', 'action': '问', 'content': '1+1=?，这是一道数学题。'}
#深度学习   回答
#  反应成   {'from': '我', 'to': '老师', 'action': '回答', 'content': '1+1=2'}

#{'from': '陌生人', 'to': '我', 'action': '问', 'content': '1+1=?'}
#  反射成   {'from': '陌生人', 'to': '我', 'action': '问', 'content': '1+1=?，这是一道数学题。'}
#深度学习   不理睬
#  反应成   {'from': '我', 'to': '陌生人', 'action': '不理睬', 'content': ''}

#{'from': '老师', 'to': '我', 'action': '问', 'content': '你喜不喜欢小美？'}
#  反射成   {'from': '德高望重的老师', 'to': '我', 'action': '问', 'content': '你喜不喜欢小美？，这是一个非常私人的问题。'}
#深度学习   不回答
#  反应成   {'from': '我', 'to': '老师', 'action': '不回答', 'content': ''}

#{'from': '妹妹', 'to': '我', 'action': '问', 'content': '你喜不喜欢小美？'}
#  反射成   {'from': '亲密的妹妹', 'to': '我', 'action': '问', 'content': '你喜不喜欢小美？，这是一个非常私人的问题。'}
#深度学习   回答
#  反应成   {'from': '我', 'to': '妹妹', 'action': '回答', 'content': '喜欢'}

#{'from': '小明', 'to': '我', 'action': '骂', 'content': '你是猪'}
#  反射成   {'from': '小明，普通的同学', 'to': '我', 'action': '骂', 'content': '你是猪，这是一句骂人的话。'}
#深度学习   回骂
#  反应成   {'from': '我', 'to': '小明', 'action': '回骂', 'content': '你才是猪'}

#{'from': '老师', 'to': '我', 'action': '骂', 'content': '你是猪'}
#  反射成   {'from': '德高望重的老师', 'to': '我', 'action': '骂', 'content': '你是猪，这是一句骂人的话。'}
#深度学习   不回骂
#  反应成   {'from': '我', 'to': '老师', 'action': '不回骂', 'content': ''}