import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


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
  ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues, vmin=0, vmax=cm.max())
  ax.set_title('Confusion Matrix')
  ax.set_xticks(range(len(classNames)), classNames, rotation=45)
  ax.set_yticks(range(len(classNames)), classNames)
  # ax.colorbar()
  ax.set_xlabel('Predicted Label')
  ax.set_ylabel('True Label')
  ax.invert_yaxis()


if __name__ == '__main__':
  true = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 2, 2]
  pred = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
  cm = getConfusionMatrix(true, pred)
  analyzeConfusionMatrix(cm)
  # plotConfusionMatrix(cm, ['0', '1', '2'], plt.subplot())
  # plt.show()
