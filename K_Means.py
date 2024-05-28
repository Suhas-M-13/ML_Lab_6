import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

X=load_iris().data
K=3

model = KMeans(n_clusters=3)
model.fit(X)
labels=model.labels_
centroids = model.cluster_centers_
print("labels : ")
print(labels)
print("Centroids : ")
print(centroids)

plt.scatter(X[:,0],X[:,1],c=labels)
plt.scatter(centroids[:,0],centroids[:,1],marker='x',color='red',s=200)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.title('K-means clustering of Iris dataset')
plt.show()