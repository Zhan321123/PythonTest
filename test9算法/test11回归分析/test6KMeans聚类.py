import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

from test1python基础.test1.test35类属性 import printObject


def kMeansTrain(data: [], nCluster: int, random_state: int = 42) -> sklearn.cluster.KMeans:
  """
  K-Means聚类算法模型训练
  :param data:
  :param nCluster:
  :param random_state:
  :return:
  """
  model = sklearn.cluster.KMeans(n_clusters=nCluster, random_state=random_state)
  model.fit(data)
  printObject(model)
  return model


def kMeansPredict(model: sklearn.cluster.KMeans, data: []) -> []:
  """
  K-Means聚类算法模型预测
  :param model:
  :param data:
  :return:
  """
  predict = model.predict(data)
  print(predict)


def showPlane(model: sklearn.cluster.KMeans, data: [], ax: plt.Axes) -> plt.Axes:
  """
  K-Means聚类算法模型可视化
  :param model:
  :param data:
  :return:
  """
  xs, ys = zip(*data)
  nClusters = model.n_clusters
  ax.scatter(xs, ys, c=model.labels_, s=50, cmap='viridis', label="clusters")
  centers = model.cluster_centers_
  ax.scatter(centers[:, 0], centers[:, 1], s=200, alpha=0.5, label="centers")
  ax.set_title('K-Means')
  ax.legend()
  return ax


if __name__ == '__main__':
  points = np.random.random((100, 2))
  print(points)
  newPoints = np.random.random((20, 2))

  m = kMeansTrain(points, 3)
  print(kMeansPredict(kMeansTrain(newPoints, 3), newPoints))

  fig, ax = plt.subplots()
  showPlane(m, points, ax)
  plt.show()
