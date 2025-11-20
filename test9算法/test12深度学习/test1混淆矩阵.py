import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def getConfusionMatrix(true, predict):
  """
  计算混淆矩阵
  :param true: 真实值
  :param predict: 预测值
  :return: 混淆矩阵
  """
  return confusion_matrix(true, predict)


def analyzeConfusionMatrix(cm: np.ndarray):
  """
  分析混淆矩阵
  :param cm:
  """
  accuracy = cm.diagonal().sum() / cm.sum()
  precisions = cm.diagonal() / (cm.sum(axis=1) + 1e-10)
  recalls = cm.diagonal() / (cm.sum(axis=0) + 1e-10)
  f1 = 2 * precisions * recalls / (precisions + recalls + 1e-10)
  print('混淆矩阵：')
  print("准确率:", accuracy)
  print("精确率:", precisions)
  print("召回率:", recalls)
  print("F1", f1)


def plotConfusionMatrix(cm: np.ndarray, classNames: list, ax: plt.Axes):
  imshow = ax.imshow(cm, cmap=plt.cm.Blues, vmin=0, vmax=cm.max(), )
  # ax.set_title('Confusion Matrix')
  # 不要边框
  for spine in ax.spines.values():
    spine.set_visible(False)
  ax.xaxis.set_tick_params(which='minor', bottom=False)
  ax.set_xticks(range(len(classNames)), classNames, rotation=90)
  ax.set_yticks(range(len(classNames)), classNames)
  plt.colorbar(imshow)
  ax.set_xlabel('Predicted Label')
  ax.set_ylabel('True Label')
  ax.set_aspect(1)
  # ax.invert_yaxis()


if __name__ == '__main__':
  true = np.random.randint(0, 10, 1000)
  pred = np.random.randint(0, 10, 1000)
  cm = getConfusionMatrix(true, pred)
  analyzeConfusionMatrix(cm)
  fig, axs = plt.subplots(1, 1)
  plotConfusionMatrix(cm, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], axs)
  plt.show()
