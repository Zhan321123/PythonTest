"""
囚徒困境游戏模型

这个游戏以两两对弈为核心互动形式（多人参与时可形成多组对弈）
每位参与者在每轮对弈中仅有两种选择——出“友好牌”（合作策略）或“敌对牌”（背叛策略），不同选择组合对应不同得分规则：
  若双方均出友好牌，两人各得+3分；
  若双方均出敌对牌，两人各得+1分；
  若一方出友好牌而另一方出敌对牌，则出友好牌的一方得0分，出敌对牌的一方得+5分。
最终可通过单轮或多轮累计得分判断个体或整体的博弈结果。
"""
import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

peoples = []
peopleNames = []
peopleCharacter = []

cheeses = ['friendly', 'enemy']


def people(define: callable):
  peoples.append(define)
  peopleNames.append(define.__name__)
  peopleCharacter.append(define.__doc__)


@people
def Cooperator(self: [str], other: [str]) -> str:
  """始终合作 (Cooperator/Cu)"""
  return 'friendly'


@people
def Defector(self: [str], other: [str]) -> str:
  """始终背叛 (Defector/Du)"""
  return 'enemy'


@people
def Random(self: [str], other: [str]) -> str:
  """随机策略 (Random)"""
  return random.choice(cheeses)


@people
def TitForTat(self: [str], other: [str]) -> str:
  """一报还一报 (Tit for Tat/TFT)"""
  if len(other) == 0:
    return "friendly"
  return other[-1]


@people
def SuspiciousTFT(self: [str], other: [str]) -> str:
  """怀疑型一报还一报 (Suspicious TFT)"""
  if len(other) == 0:
    return "enemy"
  return other[-1]


@people
def GenerousTFT(self: [str], other: [str]) -> str:
  """慷慨型一报还一报 (Generous TFT)"""
  if len(other) == 0:
    return "friendly"
  if other[-1] == 'friendly':
    return 'friendly'
  else:
    return random.choice(cheeses)


@people
def GrimTrigger(self: [str], other: [str]) -> str:
  """冷酷策略 (Grim Trigger)"""
  if len(other) == 0:
    return "friendly"
  if 'enemy' in other:
    return 'enemy'
  return 'friendly'


@people
def TwoGrimTrigger(self: [str], other: [str]) -> str:
  """两报冷酷型 (Grim Trigger)"""
  if len(other) == 0 or len(other) == 1:
    return "friendly"
  for i in range(len(other) - 1):
    if other[i] == other[i + 1] == 'enemy':
      return 'enemy'
  return 'friendly'


@people
def Contrite(self: [str], other: [str]) -> str:
  """懊悔策略 (Contrite)"""
  if len(other) == 0:
    return "friendly"
  if self[-1] == "enemy":
    return 'friendly'
  return other[-1]


@people
def TitForTwoTats(self: [str], other: [str]) -> str:
  """Tit for Two Tats (TFTT)"""
  if len(other) == 0 or len(other) == 1:
    return "friendly"
  if other[-1] == other[-2] == 'enemy':
    return 'enemy'
  return 'friendly'


@people
def TwoTitsForTat(self: [str], other: [str]) -> str:
  """Tit for Two Tats (TFTT)"""
  if len(other) == 0:
    return "friendly"
  if len(other) == 1:
    return other[-1]
  if other[-1] == 'enemy' or other[-2] == 'enemy':
    return 'enemy'
  return 'friendly'


@people
def Pavlov(self: [str], other: [str]) -> str:
  """巴甫洛夫策略 (Pavlov/Win-Stay Lose-Switch)"""
  if len(other) == 0:
    return "friendly"
  if other[-1] == self[-1]:
    return self[-1]
  else:
    return self[-1] if self[-1] != 'friendly' else 'enemy'


def play(peoples: [callable], peopleNames: [str], times: int = 100, staccato=False, selfBattle=False):
  """
  对弈过程
  :param peoples: 选手
  :param peopleNames: 选手名称
  :param times: 轮数
  :param staccato: 是否一步一步进行
  :param selfBattle: 是否自己跟自己对弈
  :return:
  """
  n = len(peoples)
  scores = np.zeros((n, n)).astype(int)
  print("开始游戏...")
  if staccato: input()
  for i in range(n):
    for j in range(i if selfBattle else i + 1, n):
      playerAName, playerBName = peopleNames[i], peopleNames[j]
      print(f'{playerAName} vs {playerBName}'.center(40, '='))
      playA, playB = peoples[i], peoples[j]
      playerACheeses, playerBCheeses = [], []
      for _ in range(times):
        a = playA(playerACheeses, playerBCheeses)
        b = playB(playerBCheeses, playerACheeses)
        playerACheeses.append(a)
        playerBCheeses.append(b)

        if a == b == 'friendly':
          scores[i][j] += 3
          scores[j][i] += 0 if i == j else 3
        elif a == b == 'enemy':
          scores[i][j] += 1
          scores[j][i] += 0 if i == j else 1
        elif a == 'friendly' and b == 'enemy':
          scores[i][j] += 0
          scores[j][i] += 0 if i == j else 5
        elif a == 'enemy' and b == 'friendly':
          scores[i][j] += 5
          scores[j][i] += 0 if i == j else 0
        else:
          raise Exception('error')
      print(f'---{playerAName}: {scores[i][j]}, {playerBName}: {scores[j][i]}---')
      if staccato:
        print(playerAName, ':', )
        print(playerACheeses)
        print(playerBName, ':', )
        print(playerBCheeses)
        input()
  print("比赛结束")
  if staccato: input()
  return scores


def figureMatrix(ax: plt.Axes, scores: [[int]], peopleNames: [str]):
  cmap = LinearSegmentedColormap.from_list('blue', [(0, '#e1eef7'), (1, '#026db3')])
  zss = np.array(scores)
  xs = np.array(peopleNames)
  ys = np.array(peopleNames)
  # pc = ax.pcolormesh(zss, cmap=cmap, linewidth=0.5,  # 格子边框宽度
  #   edgecolors='k',  # 格子边框颜色
  #   vmin=zss.min(), vmax=zss.max())  # 色值范围，大于使用max的颜色，小于使用min
  for i in range(len(xs)):
    for j in range(i, len(ys)):
      triangle1 = plt.Polygon([(i, j), (i, j + 1), (i + 1, j + 1)],
        facecolor=cmap(zss[j][i] / zss.max()), edgecolor='k', linewidth=0.5)
      triangle2 = plt.Polygon([(i, j), (i + 1, j), (i + 1, j + 1)],
        facecolor=cmap(zss[i][j] / zss.max()), edgecolor='k', linewidth=0.5)
      ax.add_patch(triangle1)
      ax.add_patch(triangle2)
      ax.text(i + 0.5 - 0.25, j + 0.5 + 0.25, zss[j][i], ha="center", va="center", color="black")
      ax.text(i + 0.5 + 0.25, j + 0.5 - 0.25, zss[i][j], ha="center", va="center", color="black")
  ax.set_aspect(1)  # 让每一格宽高一致
  ax.set_xticks(np.arange(len(xs)) + 0.5, labels=xs, rotation=90)
  ax.set_yticks(np.arange(len(ys)) + 0.5, labels=ys)
  ax.set_xlim(0, len(xs))
  ax.set_ylim(0, len(ys))
  ax.set_title("detailed record")
  ax.autoscale_view()


def figureBar(ax: plt.Axes, scoreSum: [], peopleNames: [str]):
  bar = ax.bar(peopleNames, scoreSum)
  ax.bar_label(bar)
  ax.set_title("grades")
  ax.set_ylabel('score')
  ax.set_xlabel('people')
  ax.set_xticks(np.arange(len(peopleNames)), labels=peopleNames)
  ax.set_ylim(bottom=0)
  ax.set_xticklabels(peopleNames, rotation=90, ha='right')
  ax.grid(axis='y', linestyle='--', alpha=0.7)
  ax.autoscale_view()


if __name__ == '__main__':
  print("选手以及性格: ")
  for i in range(len(peoples)):
    print(f"{peopleNames[i]}: {peopleCharacter[i]}")
  s = play(peoples, peopleNames, times=10, staccato=False)
  print(s)
  scoreSum = np.sum(s, axis=1)
  print(scoreSum)

  fig, axs = plt.subplots(1, 2)
  axs = axs.flatten()
  figureMatrix(axs[0], s, peopleNames)
  figureBar(axs[1], scoreSum, peopleNames)
  plt.show()
