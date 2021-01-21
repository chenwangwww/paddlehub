# from sklearn.metrics.cluster import homogeneity_score
# from sklearn.metrics.cluster import completeness_score

# ret = homogeneity_score([0,0,1,1], [1,1,0,0])
# print(ret)

# ret2 = homogeneity_score([0,0,1,1], [0,0,1,2])
# print(ret2)

# ret2 = homogeneity_score([0,0,1,1], [0,3,1,2])
# print(ret2)

# ret2 = homogeneity_score([0,0,1,1], [0,2,0,2])
# print(ret2)

# ret = completeness_score([0,0,1,1], [1,1,3,3])
# print(ret)

# ret = completeness_score([0,0,1,1], [1,1,3,2])
# print(ret)

# ret = completeness_score([0,0,1,1], [1,0,0,1])
# print(ret)

# from sklearn.cluster import AffinityPropagation
# from sklearn import metrics
# from sklearn.datasets import make_blobs

# centers = [[1,1], [-1, -1], [1,-1]]
# X,labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.5, random_state=0)
# af = AffinityPropagation(preference=-50).fit(X)
# cluster_centers_indices = af.cluster_centers_indices_
# labels = af.labels_
# n_clusters_ = len(cluster_centers_indices)
# print(n_clusters_)
# print("----------------")
# print(af.cluster_centers_)
# print("----------------")
# print(centers)
# print("----------------")
# print([X[val] for val in cluster_centers_indices])

import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

l = 100
x,y = np.indices((l, l))
# print(x.shape)
# print('-----------')
# print(y.shape)

center1 = (28,24)
center2 = (40,50)
center3 = (67,58)
center4 = (24,70)

radius1, radius2, radius3, radius4 = 16, 14, 15, 14

circle1 = (x - center1[0]) ** 2 + (y - center1[1]) ** 2 < radius1 ** 2
circle2 = (x - center2[0]) ** 2 + (y - center2[1]) ** 2 < radius2 ** 2
circle3 = (x - center3[0]) ** 2 + (y - center3[1]) ** 2 < radius3 ** 2
circle4 = (x - center4[0]) ** 2 + (y - center4[1]) ** 2 < radius4 ** 2

img = circle1 + circle2 + circle3 + circle4
mask = img.astype(bool)
img = img.astype(float)

img +=1 + 0.2 * np.random.randn(*img.shape)

graph = image.img_to_graph(img, mask=mask)
# print(type(graph))
print(graph.shape)
print('------------')
# print(graph.col)
print(graph.data.shape)
print('-------------')
graph.data = np.exp(-graph.data / graph.data.std())
print(graph.data)
print('-------------')
print(graph.data.shape)

print('-------------')
print(np.arange(3))