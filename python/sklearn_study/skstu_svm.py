from sklearn import svm
import numpy as np

# X = [[0,0],[1,1]]
# y = [0,1]
# clf = svm.SVC(gamma='scale')
# clf.fit(X, y)
# predict = clf.predict([[-10,-10]])
# print(predict)
# print(clf.support_vectors_)
# print(clf.support_)
# print(clf.n_support_)

# X = [[0,0], [2,2]]
# y = [0.5, 2.5]
# clf = svm.SVR()
# clf.fit(X, y)
# print(clf.predict([[-2,-2]]))

x = np.array([[1], [2], [3]])
y = np.array([[2,3]])
print(np.dot(x,y))