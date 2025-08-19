import os


def getDirsFiles(dirPath: str) -> [str]:
  """获取一个文件夹下所有文件"""
  result = [os.path.join(dirPath, i) for i in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, i))]
  result.sort()
  return result


def renameAllFiles(dirPath: str, newNames: [str]) -> None:
  """批量重命名文件夹下的所有文件"""
  for file, newName in zip(getDirsFiles(dirPath), newNames[:len(getDirsFiles(dirPath))]):
    suffix = os.path.splitext(file)[-1]
    newName = str(newName)
    if not newName.endswith(suffix):
      newName += '.' + suffix
    os.rename(file, os.path.join(dirPath, newName))


if __name__ == '__main__':
  dirPath = r'1'
  print(getDirsFiles(dirPath))
  renameAllFiles(dirPath, [f"figure{i}.png" for i in range(1, 50)])
