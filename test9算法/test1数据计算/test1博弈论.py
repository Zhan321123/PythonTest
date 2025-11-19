"""
gameTheory
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
def zhangsan(self: [str], other: [str]) -> str:
  """随便，无所谓"""
  return random.choice(cheeses)


@people
def lisi(self: [str], other: [str]) -> str:
  """看你最近对我是什么态度"""
  if len(other) == 0:
    return 'friendly'
  return other[-1]


@people
def wangwu(self: [str], other: [str]) -> str:
  """校霸，谁都要让着我"""
  return 'enemy'


@people
def zhaoliu(self: [str], other: [str]) -> str:
  """老好人"""
  return 'friendly'


def play(peoples: [callable], peopleNames: [str], times: int = 100, staccato=False):
  n = len(peoples)
  scores = np.zeros((n, n)).astype(int)
  print("开始游戏...")
  if staccato: input()
  for i in range(n):
    for j in range(i + 1, n):
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
          scores[j][i] += 0 if i == j else 5
        elif a == 'enemy' and b == 'friendly':
          scores[j][i] += 5
        else:
          raise Exception('error')
      print(f'---{playerAName}: {scores[i][j]}, {playerBName}: {scores[j][i]}---')
      if staccato:
        print(playerAName,':',)
        print(playerACheeses)
        print(playerBName,':',)
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
  pc = ax.pcolormesh(zss, cmap=cmap, linewidth=0.5,  # 格子边框宽度
    edgecolors='k',  # 格子边框颜色
    vmin=zss.min(), vmax=zss.max())  # 色值范围，大于使用max的颜色，小于使用min
  # fig.colorbar(pc, ax=ax, pad=0.05, shrink=1)  # 给ax添加色带
  for i in range(len(xs)):
    for j in range(len(ys)):
      ax.text(j + 0.5, i + 0.5, zss[i][j], ha="center", va="center", color="black", fontsize=18)
  ax.set_aspect(1)  # 让每一格宽高一致
  ax.set_xticks(np.arange(len(xs)) + 0.5, labels=xs, fontsize=14)
  ax.set_yticks(np.arange(len(ys)) + 0.5, labels=ys, fontsize=14)
  ax.set_title("detailed record")


def figureBar(ax: plt.Axes, scoreSum: [], peopleNames: [str]):
  bar = ax.bar(peopleNames, scoreSum)
  ax.bar_label(bar)
  ax.set_title("grades")
  ax.set_ylabel('score')
  ax.set_xlabel('people')
  ax.set_xticks(np.arange(len(peopleNames)), labels=peopleNames)
  ax.set_ylim(0)


if __name__ == '__main__':
  print("选手以及性格: ")
  for i in range(len(peoples)):
    print(f"{peopleNames[i]}: {peopleCharacter[i]}")
  s = play(peoples, peopleNames,times=1000, staccato=False)
  print(s)
  scoreSum = np.sum(s, axis=1)
  print(scoreSum)

  fig, axs = plt.subplots(1, 2)
  axs = axs.flatten()
  figureMatrix(axs[0], s, peopleNames)
  figureBar(axs[1], scoreSum, peopleNames)
  plt.show()
