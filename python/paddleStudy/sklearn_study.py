# from sklearn import datasets
# from sklearn.multiclass import OneVsRestClassifier
# from sklearn.svm import LinearSVC
# iris = datasets.load_iris()
# X, y = iris["data"], iris["target"]
# result = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X,y).predict(X)
# print(result)

# from sklearn.datasets import load_iris
# data = load_iris()

# print(u'%s\tlabel' % (u'\t'.join(data.feature_names)))
# for sample_data, sample_label in zip(data.data, data.target):
#     sample_data_str = u'\t'.join([str(w) for w in sample_data])
#     sample_label_str = data.target_names[sample_label]
#     print("%s\t%s" % (sample_data_str, sample_label_str))

# from sklearn import datasets
# X,y = datasets.make_regression(n_samples=10, n_features=1, n_targets=1, noise=1)

# import matplotlib.pyplot as plt
# plt.figure()
# plt.scatter(X, y)
# plt.show()

# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier

# iris = datasets.load_iris()
# iris_X = iris.data
# iris_y = iris.target
# X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
# print(X_test)
# print(y_test)
# knn = KNeighborsClassifier()
# knn.fit(X_train, y_train)
# print(knn.predict(X_test))
# print('____________________________')
# print(y_test)

# from sklearn.datasets._samples_generator import make_classification

# X,y = make_classification(n_samples=10, n_features=2, scale=100, n_redundant=0)
# print(X)
# print(y)

# from sklearn import datasets
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import cross_val_score
# import matplotlib.pyplot as plt

# iris = datasets.load_iris()
# X = iris['data']
# y = iris['target']
# k_range = range(1,31)
# k_score = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     scores = cross_val_score(knn, X, y, cv = 10, scoring='accuracy')
#     k_score.append(scores.mean())
# plt.figure()
# plt.plot(k_range, k_score)
# plt.xlabel('value of k for KNN')
# plt.ylabel('CrossValidation accuracy')
# plt.show()

# from sklearn.svm import SVC

# from sklearn.datasets import load_digits
# import numpy as np

# digits = load_digits()
# print(digits.keys())
# print(digits['DESCR'])
# print(len(digits['target']))
# print(np.array(digits['data']).shape)
# print(digits['images'][0])

# from sklearn.datasets import fetch_openml
# import numpy as np
# mice = fetch_openml(name='MiceProtein', version=4)
# print(mice.data.shape)
# print(mice.target.shape)
# print(np.unique(mice.target))
# mice = fetch_openml(data_id=40966)
# print(mice.DESCR)

# from sklearn.datasets import load_diabetes
# import matplotlib.pyplot as plt
# dia = load_diabetes()
# print(np.unique(dia.target).shape)
# print(dia.feature_names)

# from sklearn.datasets import fetch_olivetti_faces
# faces = fetch_olivetti_faces()
# # print(faces.DESCR)
# print(faces.data[0])
# print(faces.images[0])


# from sklearn import linear_model
# reg = linear_model.Ridge(alpha=.5)
# reg.fit([[0,0], [0,0], [1,1]], [0, .1, 1])
# print(reg.coef_)
# print(reg.intercept_)

#最近邻分类算法
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# import numpy as np

# X_train = np.array([[6], [7], [8], [11], [12], [13], [17], [18], [19]])
# y_train = np.array([0,0,0,1,1,1,2,2,2])

# X_test = np.array([[5], [7], [11], [12], [17], [20]])
# y_test = np.array([0,0,1,1,2,2])

# knn = KNeighborsClassifier()
# knn.fit(X_train, y_train)
# print(knn.predict(X_test))
# print('____________________________')
# print(y_test)

# import numpy as np
# from sklearn.datasets import load_digits

# data, labels = load_digits(return_X_y=True)
# (n_samples, n_features), n_digits = data.shape, np.unique(labels).size

# print(f"# digits:{n_digits}; # samples:{n_samples}; # features:{n_features}")

# from sklearn.cluster import KMeans
# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt

# reduced_data = PCA(n_components=2).fit_transform(data)
# print(reduced_data)
# kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
# kmeans.fit(reduced_data)

# h = .02

# x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
# y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# print(x_min, x_max)
# print(y_min, y_max)
# print(xx.shape)
# print("---------------")
# print(yy.shape)
# Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
# print(Z)
# print(Z.shape)
# Z = Z.reshape(xx.shape)
# plt.figure(1)
# plt.clf()
# plt.imshow(Z, interpolation="nearest", extent=(xx.min(), xx.max(), yy.min(), yy.max()), cmap=plt.cm.Paired, aspect="auto", origin="lower")
# plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# centroids = kmeans.cluster_centers_
# plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=169, linewidths=3, color="w", zorder=10)
# plt.title("k-means\ncross")
# plt.xlim(x_min, x_max)
# plt.ylim(y_min, y_max)
# plt.xticks(())
# plt.yticks(())
# plt.show()

# data = np.arange(-1, 2.1, 0.5)
# print(data)

# x = np.array([1,2,3])
# y = np.array([4,5,6,7])
# xv, yv = np.meshgrid(x, y)
# print(xv)
# print("----------------")
# print(yv)
# print("----------------")
# print(xv.ravel())
# print("----------------")
# print(yv.ravel())
# print("----------------")
# print(np.c_[xv.ravel(), yv.ravel()])


#K-均值聚类算法
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn.decomposition import PCA

# data, labels = datasets.load_digits(return_X_y=True)
# (n_samples, n_features), n_digits = data.shape, np.unique(labels).size
# reduced_data = PCA(n_components=2).fit_transform(data)
# X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.02)

# X_train = np.array([[6], [7], [8], [11], [12], [13], [17], [18], [19]])
# y_train = np.array([0,0,0,1,1,1,2,2,2])

# X_test = np.array([[5], [7], [11], [12], [17], [20]])
# y_test = np.array([0,0,1,1,2,2])

# kmeans = KMeans(init="k-means++", n_clusters=3, n_init=10)
# kmeans.fit(X_train)

# Z = kmeans.predict(X_test)

# print(Z)
# print("------------")
# print(y_test)
# print("------------")
# print(kmeans.cluster_centers_)

import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs

centers = [[1,1], [-1,-1], [1,-1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print(n_clusters_)

import matplotlib.pyplot as plt
from itertools import cycle

plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
plt.title('mean shift')
plt.show()