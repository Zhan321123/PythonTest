import matplotlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import export_text, plot_tree
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


def decisionTreeTrain(
    dataXs: dict[str, list],
    dataY: dict[str, list],
    test_size: float = 0.2,
    random_state: int = 42,
    modelParams: dict = {"criterion": "entropy", "max_depth": 3}
) -> (DecisionTreeClassifier, dict[str, LabelEncoder]):
  """
  训练决策树模型

  :param dataXs: 自变量字典，格式为{自变量名:[值列表], ...}
  :param dataY: 因变量字典，格式为{因变量名:[值列表]}
  :param test_size: 测试集占比
  :param random_state: 随机数种子
  :param modelParams: 决策树模型参数: {
      criterion: 评价标准，'gini', 'entropy'
      max_depth: 树深度
    }
  :return: (决策树模型, 标签编码器字典)
  """
  # 检查数据长度是否一致
  lengths = [len(vals) for vals in dataXs.values()]
  dep_length = len(next(iter(dataY.values())))
  if not all(l == dep_length for l in lengths):
    raise ValueError("所有变量的样本数量必须一致")

  # 转换为DataFrame
  X = pd.DataFrame(dataXs)
  y = pd.DataFrame(dataY)
  dep_var_name = y.columns[0]
  y = y[dep_var_name]

  # 初始化标签编码器
  label_encoders: dict[str, LabelEncoder] = {}

  # 对所有分类特征进行编码
  for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

  # 对因变量进行编码
  le_dep = LabelEncoder()
  y_encoded = le_dep.fit_transform(y)
  label_encoders[dep_var_name] = le_dep

  # 划分训练集和测试集
  X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=test_size, random_state=random_state
  )

  # 创建并训练决策树模型
  clf = DecisionTreeClassifier(**modelParams, random_state=random_state)
  clf.fit(X_train, y_train)

  # 模型评估
  y_pred = clf.predict(X_test)

  print("模型评估结果：")
  print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")
  print("\n混淆矩阵:")
  print(confusion_matrix(y_test, y_pred))
  print("\n分类报告:")
  print(classification_report(
    y_test,
    y_pred,
    target_names=le_dep.classes_
  ))

  # 输出决策树结构
  print("\n决策树结构:")
  tree_rules = export_text(clf, feature_names=list(X.columns))
  print(tree_rules)

  return clf, label_encoders


def decisionTreeVisualize(
    ax: plt.Axes,
    clf: DecisionTreeClassifier,
    label_encoders: dict[str, LabelEncoder],
) -> plt.Axes:
  """
  可视化决策树

  :param ax:
  :param clf: 决策树模型
  :param label_encoders: 标签编码器字典
  :return:
  """
  # 获取特征名称
  feature_names = [name for name in label_encoders.keys()
                   if name not in next(iter(label_encoders.values())).classes_]

  # 获取因变量名称和类别
  dep_var_name = None
  class_names = None
  for name, le in label_encoders.items():
    if name not in feature_names:
      dep_var_name = name
      class_names = list(le.classes_)
      break

  # 绘制决策树
  plot_tree(
    clf,
    ax=ax,
    feature_names=feature_names,
    class_names=class_names,
    filled=True,
    rounded=True,
    proportion=True,
    node_ids=True,
    fontsize=10
  )

  if dep_var_name:
    ax.set_title(f'决策树可视化（目标变量：{dep_var_name}）', fontsize=12)

  return ax


def decisionTreePredict(
    newData: dict[str, list],
    clf: DecisionTreeClassifier,
    label_encoders: dict[str, LabelEncoder],
    return_proba: bool = False
) -> dict[str, list]:
  """
  对新数据进行预测

  :param newData: 新数据字典，格式为{自变量名:[值列表], ...}
  :param clf: 决策树模型
  :param label_encoders: 标签编码器字典
  :param return_proba: 是否返回预测概率
  :return: 预测结果字典，包含预测类别和可选的概率
  """
  if not newData:
    raise ValueError("新数据不能为空")

  # 转换为DataFrame
  X_new = pd.DataFrame(newData)

  # 检查特征是否匹配
  feature_names = [name for name in label_encoders.keys()
                   if name not in next(iter(label_encoders.values())).classes_]
  for feature in feature_names:
    if feature not in X_new.columns:
      raise ValueError(f"新数据缺少必要特征: {feature}")

  # 对新数据进行编码
  for col in X_new.columns:
    if col in label_encoders:
      le = label_encoders[col]
      # 检查新数据中是否有未见过的类别
      for val in X_new[col]:
        if val not in le.classes_:
          raise ValueError(f"特征'{col}'包含未见过的类别: {val}")
      X_new[col] = le.transform(X_new[col])

  # 预测
  predictions = clf.predict(X_new)

  # 解码预测结果
  dep_var_name = None
  for name, le in label_encoders.items():
    if name not in feature_names:
      dep_var_name = name
      predictions_decoded = le.inverse_transform(predictions)
      break

  if dep_var_name is None:
    raise ValueError("无法确定因变量名称")

  # 准备结果
  result: dict[str, list] = {
    f"{dep_var_name}_预测结果": predictions_decoded.tolist()
  }

  # 如果需要，返回预测概率
  if return_proba:
    probabilities = clf.predict_proba(X_new)
    result[f"{dep_var_name}_预测概率"] = probabilities.tolist()
    result[f"概率对应的类别"] = list(label_encoders[dep_var_name].classes_)

  return result


if __name__ == '__main__':
  dataX = {
    '年龄': ['青年', '青年', '中年', '老年', '老年', '老年', '中年', '青年', '青年', '老年'],
    '收入水平': ['低', '低', '低', '中', '高', '高', '高', '中', '高', '中'],
    '是否有车': ['否', '是', '否', '否', '是', '否', '是', '否', '是', '是'],
  }
  dataY = {
    '是否购买': ['否', '否', '是', '是', '是', '否', '是', '否', '是', '是']
  }
  clf, label_encoders = decisionTreeTrain(dataX, dataY)
  plt.figure(figsize=(15, 10))
  decisionTreeVisualize(plt.gca(), clf, label_encoders)
  plt.show()
  print(decisionTreePredict(
    {
      '年龄': ['青年'],
      '收入水平': ['高'],
      '是否有车': ['是']
    },
    clf, label_encoders
  ))
