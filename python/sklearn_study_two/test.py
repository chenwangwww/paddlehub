# lines = {'d':1, 's':'ch'}
# t = filter(lambda key:lines[key] == 1, lines)
# print(dict(t))
# ted = 11
# class test:
    
#     def __init__(self):
#         pass
#     def t(self):
#         print(ted)

# t = test()
# t.t()

# from ltp import LTP
# ltp = LTP()

# seg, hidden = ltp.seg(['北京的景区有长城、故宫'])
# pos = ltp.pos(hidden)
# srl = ltp.srl(hidden, keep_empty=False)

# print(seg)
# print(pos)
# print(srl)

# from enum import Enum
# month = Enum('Month', ('Jan', 'Feb'))
# print(month.Jan)

# class NeureCtr:
#     def __init__(self, id):
#         self._uuid = id
#         self._relevants = {}

#     @property
#     def relevants(self):
#         return self._relevants
#     @relevants.setter
#     def relevants(self, value):
#         if value[0] not in self._relevants:
#             self._relevants[value[0]] = [value[1]]
#         else:
#             info = self._relevants[value[0]]
#             info.append(value[1])
            

# def testFunc(a):
#     if a:
#         return "1", "2"

# a = testFunc('1')
# print(a)

# var = "VALUES(%s)" % 1
# print(var)


# b=b'\xe9\x80\x86\xe7\x81\xab'
# string=str(b,'utf-8')
# print(string)

# import requests
# from bs4 import BeautifulSoup

# geography_url = 'https://you.ctrip.com/searchsite/Sight?query='

# def crawl_geo(location):
#     url = geography_url + location + '&PageNo=1'
#     strhtml = requests.get(url)
#     soup = BeautifulSoup(strhtml.text, 'lxml')
#     search_list = soup.select('body > div.content.cf > div.main > div.search-content.cf > div > div.result > ul > li > dl > dt > a')
#     if len(search_list) == 0:
#         pass
#     else:
#         geo_list = search_list[::2]
#         loc_list = search_list[1::2]
#         for i in range(len(geo_list)):
#             res = {}
#             res['geo'] = geo_list[i].get_text()
#             res['geo_link'] = geo_list[i].get('href')
#             res['loc'] = loc_list[i].get_text()
#             res['loc_link'] = loc_list[i].get('href')
#             print(res)
#             print('--------------')

# crawl_geo('北京')


# a = input("input:")
# print(type(a))

from pyDatalog import pyDatalog

# pyDatalog.create_terms('X,Y')
# res = (X==True) & (X==False)
# print(res)
# print(type(res))

# pyDatalog.create_terms('X,Y,Z,salary,tax_rate,tax_rate_for_salary_above,net_salary')
# salary['foo'] = 60
# salary['bar'] = 110
# print(salary[X]==Y)
# _salary = dict()
# _salary['foo'] = 60
# _salary['bar'] = 110
# print(_salary.items())

# (tax_rate_for_salary_above[X] == 0.33) <= (0 <= X)
# (tax_rate_for_salary_above[X] == 0.5) <= (100 <= X)
# print(tax_rate_for_salary_above[150]==Y)

# pyDatalog.create_terms('factorial, N')
# factorial[N] = N * factorial[N-1]
# factorial[1] = 1
# print(N==factorial[3])

# pyDatalog.create_terms('X,Y,manager,count_of_direct_reports')
# +(manager['Mary']=='John')
# +(manager['Sam'] == 'Mary')
# +(manager['Tom'] == 'Mary')
# (count_of_direct_reports[X] == len_(Y)) <= (manager[Y]==X)
# print(count_of_direct_reports['Mary']==X)

# pyDatalog.create_terms('X,Y,Z,works_in,department_size,manager,indirect_manager,count_of indirect_reports')
# +works_in('Mary', 'Production')
# +works_in('Sam', 'Marketing')
# +works_in('John', 'Production')
# +works_in('John', 'Marketing')
# print(works_in(X, 'Production'))

# _works_in = set()
# _works_in.add(('Mary', 'Production'))
# _works_in.add(('Sam', 'Marketing'))
# _works_in.add(('John', 'Production'))
# _works_in.add(('John', 'Marketing'))
# for i in _works_in:
#     if i[1]=='Production':
#         print(i[0])

# pyDatalog.create_terms('X,Y,Z,works_in,department_size,manager,indirect_manager,count_of_indirect_reports')
# +(manager['Mary']=='John')
# +(manager['Sam'] == 'Mary')
# +(manager['Tom'] == 'Mary')
# -(manager['Mary'] == 'John')
# indirect_manager(X,Y) <= (manager[X] == Y)
# indirect_manager(X,Y) <= (manager[X] == Z) & indirect_manager(Z,Y)
# print(indirect_manager('Sam', X))
# (count_of_indirect_reports[X]==len_(Y)) <= indirect_manager(Y,X)
# print(count_of_indirect_reports['John']==Y)
# print(indirect_manager(X, 'John'))

# pyDatalog.create_terms('X,Y,Z,link,can_reach')
# +link(1,2)
# +link(2,3)
# +link(2,4)
# +link(2,5)
# +link(5,6)
# +link(6,7)
# +link(7,2)

# link(X,Y) <= link(Y,X)
# can_reach(X,Y) <= link(X,Y)
# can_reach(X,Y) <= link(X,Z) & can_reach(Z,Y) & (X!=Y)
# print(can_reach(1,Y))

# pyDatalog.create_terms('N,X0,X1,X2,X3,X4,X5,X6,X7')
# pyDatalog.create_terms('ok,queens,next_queen')

# queens(X0) <= (X0._in(range(8)))

# queens(X0,X1) <= queens(X0) & next_queen(X0,X1)
# queens(X0,X1,X2) <= queens(X0,X1) & next_queen(X0,X1,X2)
# queens(X0,X1,X2,X3) <= queens(X0,X1,X2) & next_queen(X0,X1,X2,X3)
# queens(X0,X1,X2,X3,X4)          <= queens(X0,X1,X2,X3)          & next_queen(X0,X1,X2,X3,X4)
# queens(X0,X1,X2,X3,X4,X5)       <= queens(X0,X1,X2,X3,X4)       & next_queen(X0,X1,X2,X3,X4,X5)
# queens(X0,X1,X2,X3,X4,X5,X6)    <= queens(X0,X1,X2,X3,X4,X5)    & next_queen(X0,X1,X2,X3,X4,X5,X6)
# queens(X0,X1,X2,X3,X4,X5,X6,X7) <= queens(X0,X1,X2,X3,X4,X5,X6) & next_queen(X0,X1,X2,X3,X4,X5,X6,X7)

# next_queen(X0,X1)                   <= queens(X1)                       & ok(X0,1,X1)
# next_queen(X0,X1,X2)                <= next_queen(X1,X2)                & ok(X0,2,X2)
# next_queen(X0,X1,X2,X3)             <= next_queen(X1,X2,X3)             & ok(X0,3,X3)
# next_queen(X0,X1,X2,X3,X4)          <= next_queen(X1,X2,X3,X4)          & ok(X0,4,X4)
# next_queen(X0,X1,X2,X3,X4,X5)       <= next_queen(X1,X2,X3,X4,X5)       & ok(X0,5,X5)
# next_queen(X0,X1,X2,X3,X4,X5,X6)    <= next_queen(X1,X2,X3,X4,X5,X6)    & ok(X0,6,X6)
# next_queen(X0,X1,X2,X3,X4,X5,X6,X7) <= next_queen(X1,X2,X3,X4,X5,X6,X7) & ok(X0,7,X7)

# ok(X1, N, X2) <= (X1 != X2) & (X1 != X2+N) & (X1 != X2-N)
# print(len(queens(X0,X1,X2,X3,X4,X5,X6,X7).data))

#北京是中国的首都
# pyDatalog.create_terms('X, Y, 北京, 上海')
# +北京('是', '中国的首都')

#上海是中国的首都吗？
# pyDatalog.create_terms('上海')
# try:
#     res = len(上海('是', '中国的首都')) != 0
# except:
#     res = False
# finally:
#     print(res)

#北京有长城和故宫
# pyDatalog.create_terms('北京')
# +北京('有', '长城')
# +北京('有', '故宫')

#北京有西湖吗？
# pyDatalog.create_terms('北京')
# try:
#     res = len(北京('有', '西湖')) != 0
# except:
#     res = False
# finally:
#     print(res)

# st = '123456'
# print(st[1:])

strr = "name:%s, id:%s" % (12, 'www')
print(strr)