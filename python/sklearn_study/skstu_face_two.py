from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
import numpy as np

# lens = len(np.unique(faces.target))
# print(lens)
# faces = datasets.fetch_olivetti_faces()
faces = fetch_lfw_people(min_faces_per_person=60)
X = faces.data
y = faces.target

X_train, X_test, y_train, y_test = train_test_split(X, y)

clf = SVC(kernel="linear")
clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)
# for pre in y_predict:
#     print(pre)
# print('----------------')
# for te in y_test:
#     print(te)
# print('----------------')
print(accuracy_score(y_test, y_predict))


# i = 0
# plt.figure(figsize=(20, 20))
# for img in faces.images:
#     plt.subplot(20,20,i+1)
#     plt.imshow(img, cmap="gray")
#     plt.xticks([])
#     plt.yticks([])
#     plt.xlabel(faces.target[i])
#     i += 1

# plt.show()