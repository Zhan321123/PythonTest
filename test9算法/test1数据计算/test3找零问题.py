"""
给定面额、找零数，求最小硬币数
"""


def change(money: int, coins: list[int]) -> (int, list[int]):
  """
  找零-贪心
  :param money: 找零数
  :param coins: 所有硬币面额数
  :return: (硬币数, 每种硬币数量)
  """
  n_coins = [0] * len(coins)

  coins = sorted(coins, reverse=True)
  n = 0
  while True:
    while coins[n] <= money:
      money -= coins[n]
      n_coins[n] += 1
    if money > 0 and n < len(coins) - 1:
      n += 1
    else:
      break
  if money > 0:
    print("未找开")
  return sum(n_coins), n_coins


if __name__ == '__main__':
  print(change(2825657, [17, 5, 20, 50, 100]))
