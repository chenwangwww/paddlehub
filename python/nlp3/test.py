from ltp import LTP
ltp = LTP()

sentence = "他是你爸爸吗？"
seg, hidden = ltp.seg([sentence])
pos = ltp.pos(hidden)
srl = ltp.srl(hidden, keep_empty=False)
dep = ltp.dep(hidden)
print(seg)
print(pos)
print(srl)
print(dep)