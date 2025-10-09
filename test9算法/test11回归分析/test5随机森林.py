# 导入必要的库
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

from test1python基础.test1.test35类属性 import printObject


def randomForestTrain(dataX: dict[str:list], dataY: dict[str:list], test_size: float = 0.2,
    random_state: int = 42, modelParams: dict = {"n_estimators": 3}) -> RandomForestClassifier:
  """
  训练随机森林模型
  :param dataX: 自变量字典, {自变量名:[值列表], ...}
  :param dataY: 因变量字典, {因变量名:[值列表]}
  :param test_size: 测试集占比
  :param random_state: 随机数种子
  :param modelParams: 随机森林模型参数: {
      e_stimators: 树数量
    }
  :return: 随机森林模型
  """
  dfx = pd.DataFrame(dataX)
  dfy = pd.DataFrame(dataY)
  X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.2, random_state=42)

  rf = RandomForestClassifier(**modelParams, random_state=random_state)
  rf.fit(X_train, y_train)
  y_pred = rf.predict(X_test)
  print("\n测试集预测结果：")
  print(f"真实标签：{y_test.values}")
  print(f"预测标签：{y_pred}")
  print(f"准确率：{accuracy_score(y_test, y_pred):.2f}")
  print("\n分类报告：")
  print(classification_report(y_test, y_pred))

  return rf


def randomForestPredict(dataX: dict[str:list], model: RandomForestClassifier) -> dict[str:list]:
  """
  随机森林模型对数据进行预测
  :param dataX: 自变量字典, {自变量名:[值列表], ...}
  :param model: 随机森林模型
  :return: 预测结果字典, {预测标签:[值列表], ...}
  """
  dfx = pd.DataFrame(dataX)
  y_pred = model.predict(dfx)
  return {
    '预测标签': y_pred.tolist()
  }


def showFeatureImportance(ax: plt.Axes, model: RandomForestClassifier) -> plt.Axes:
  """
  显示随机森林模型特征重要性
  :param ax:
  :param model: 随机森林模型
  """
  xlabels = model.feature_names_in_
  importance = model.feature_importances_
  ax.bar(xlabels, importance)
  ax.set_title('特征重要性')
  ax.set_xlabel('特征')
  ax.set_ylabel('重要性')
  return ax


if __name__ == '__main__':
  xs = {
    '颜色': [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    '形状': [0, 0, 1, 1, 0.5, 0, 0, 1, 1, 0],  # 0.5表示略椭圆
    '重量': [180, 160, 140, 150, 170, 130, 190, 160, 150, 140],
    '表皮纹理': [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
  }
  ys = {'标签': [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]}  # 0=苹果，1=橙子

  xs2 = {
    "颜色": [1, 0, 1],
    "形状": [0.5, 1, 0.5],
    "重量": [180, 100, 140],
    "表皮纹理": [0, 0, 1]
  }

  model = randomForestTrain(xs, ys)
  print(randomForestPredict(xs2, model))

  fig, ax = plt.subplots()
  showFeatureImportance(ax, model)
  plt.show()
