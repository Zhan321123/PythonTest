"""
树

二叉树
二叉搜索树/二叉查找树
深度优先遍历
  先序遍历/前序遍历（根 -> 左 -> 右）
  后序遍历（左 -> 右 -> 根）
  中序遍历（左 -> 根 -> 右）

广度优先遍历（从上到下，从左到右）
"""


class MultiTreeNode:
  """
  多叉树
  """

  def __init__(self, value):
    self.value = value
    self.children = []
    self.parent = None
    self.length = 0

  def addChild(self, child: "MultiTreeNode"):
    """新增子节点"""
    self.children.append(child)
    child.parent = self
    self.length += 1

  def getSize(self):
    """获取节点大小（包含子节点）"""
    size = self.length
    for child in self.children:
      size += child.getSize()
    return size

  def traverse(self):
    """遍历节点"""
    result = [self.value]
    for child in self.children:
      result.append(child.value)
      result.extend(child.traverse())
    return result

  def __iter__(self):
    yield self
    for child in self.children:
      yield from child

  def deleteChild(self, child: "MultiTreeNode"):
    """删除子节点"""
    self.children.remove(child)
    child.parent = None
    self.length -= 1

  def isRoot(self):
    """判断是否为根节点"""
    return self.parent is None

  def isLeaf(self):
    """判断是否为叶子节点"""
    return self.length == 0

  def getLevel(self):
    """获取节点层级（根节点层级为0）"""
    level = 0
    current = self
    while not current.isRoot():
      level += 1
      current = current.parent
    return level

  def getPath(self):
    """获取从根节点到当前节点的路径（值列表）"""
    path = []
    current = self
    while current:
      path.insert(0, current.value)
      current = current.parent
    return path

  def __contains__(self, item):
    return item in [node.value for node in self]

  def __repr__(self):
    return f"TreeNode({self.value})"


class SearchTreeNode:
  """
  二叉搜索树
  """

  def __init__(self, value):
    self.value = value
    # TODO

class BTreeNode:
  """
  多路平衡查找树/B-树
  TODO
  """

if __name__ == '__main__':
  minecraft = MultiTreeNode('minecraft')
  versions = MultiTreeNode('versions')
  assets = MultiTreeNode('assets')
  libraries = MultiTreeNode('libraries')
  mc1201 = MultiTreeNode('1.20.1')
  mc1182 = MultiTreeNode('1.18.2')
  mc1192 = MultiTreeNode('1.19.2')
  saves = MultiTreeNode('saves')
  mods = MultiTreeNode('mods')

  minecraft.addChild(versions)
  minecraft.addChild(assets)
  minecraft.addChild(libraries)
  versions.addChild(mc1201)
  versions.addChild(mc1182)
  versions.addChild(mc1192)
  mc1201.addChild(saves)
  mc1201.addChild(mods)

  print(minecraft.traverse())
  for i in minecraft:
    print(i.value, end=' ')
  print()
  print(minecraft.getSize())
