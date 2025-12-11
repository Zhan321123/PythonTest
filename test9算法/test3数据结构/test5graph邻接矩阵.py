class MatrixGraph:
  """
  单向关系图/邻接矩阵图
  TODO

  适用于元素较少的场景，且较少删改
  """

  def __init__(self, vertices):
    self.vertices = [i for i in vertices]
    self.length = len(vertices)
    self.matrix = [[None for _ in range(self.length)] for _ in range(self.length)]

  def addVertex(self, value):
    """添加顶点元素"""

  def addEdge(self, value1, value2, edge):
    """添加顶点之间的关系，value1指向value2"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')
    self.matrix[self.vertices.index(value1)][self.vertices.index(value2)] = edge

  def getEdge(self, value1, value2):
    """获取两个顶点关系，value1指向value2"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')
    return self.matrix[self.vertices.index(value1)][self.vertices.index(value2)]

  def deleteVertex(self, value):
    """删除顶点"""

  def deleteEdge(self, value1, value2):
    """删除关系"""

  def getNeighbors(self, value):
    """获取与该顶点有关的元素"""


if __name__ == '__main__':
  people = ["自己", "父亲", "母亲", "爷爷", ]
  calls = [
    [None, "爸爸", "妈妈", "爷爷"],
    ["儿子", None, "老婆", "爸爸"],
    ["儿子", "老公", None, "爸爸"],
    ["孙子", "儿子", "儿媳", None],
  ]
  mg = MatrixGraph(people)
  mg.matrix = calls
  print(mg.getEdge("自己", "母亲"))
