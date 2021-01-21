import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]])
pca = PCA(svd_solver='arpack')
pca.fit(X)
print(pca.n_components_)
print(pca.n_features_)
print(pca.n_samples_)
print(pca.explained_variance_ratio_)
print(pca.singular_values_)