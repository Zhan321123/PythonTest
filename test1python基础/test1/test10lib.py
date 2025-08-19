import importlib.metadata


def generatePipInstallCommand(filterPackager: set[str] = None, excludePackager: set[str] = {'pip'}) -> str:
  """
  获取当前环境中已安装的库及其版本，生成 pip install 命令

  :param excludePackager: 排除的包名
  :param filterPackager: 需要过滤的包名

  """
  # 获取所有已安装的包及其版本
  dists = list(importlib.metadata.distributions())
  packageNames = [dist.metadata['Name'].lower() for dist in dists]
  packageVersions = [dist.version for dist in dists]

  if filterPackager is None:
    filterPackager = set(packageNames)
  else:
    filterPackager = {pack.lower() for pack in filterPackager}

  # 筛选package
  result = {}
  for p, v in zip(packageNames, packageVersions):
    if p in filterPackager and p not in excludePackager:
      result[p] = v

  # 生成 pip 安装命令
  pip_command = "pip install " + " ".join([f"{p}=={v}" for p, v in result.items()])
  return pip_command


if __name__ == "__main__":
  command = generatePipInstallCommand()

  print("生成的 pip 安装命令：")
  print(command)
