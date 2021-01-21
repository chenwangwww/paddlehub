import pandas as pd
from sklearn import preprocessing

# s = pd.Series(['a','b','c','a'])
# w = pd.get_dummies(s, drop_first=True, sparse=True)
# print(w)

# enc = preprocessing.OneHotEncoder()
# enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
# arr = enc.transform([[1,0,3]]).toarray()
# print(arr)

genders = ['female', 'male']
locations = ['from Africa', 'from Asia', 'from Europe', 'from US']
browsers = ['uses Chrome', 'uses Firefox', 'uses IE', 'uses Safari']
enc = preprocessing.OneHotEncoder(categories=[genders, locations, browsers])
X = [['male', 'from US', 'uses Safari'], ['female', 'from Europe', 'uses Firefox']]
enc.fit(X)
arr = enc.transform([['female', 'from Asia', 'uses Chrome']]).toarray()
print(arr)