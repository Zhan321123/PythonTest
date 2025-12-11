class DoubleRelationGraph:
  """
  双向关系图/邻接表图

  适用于频繁增删改查
  """

  class _DoubleRelationVertex:
    """
    顶点
    """

    def __init__(self, value):
      self.value = value
      self.edges = dict()

    def addEdge(self, other: "DoubleRelationGraph._DoubleRelationVertex", weight):
      self.edges[other] = weight

  def __init__(self):
    self.vertices = dict()

  def addVertex(self, value):
    """添加顶点元素"""
    if value in self.vertices:
      raise ValueError('顶点已存在')
    self.vertices[value] = DoubleRelationGraph._DoubleRelationVertex(value)

  def addEdge(self, value1, value2, weight):
    """添加顶点之间的关系"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')
    self.vertices[value1].addEdge(self.vertices[value2], weight)
    self.vertices[value2].addEdge(self.vertices[value1], weight)

  def getEdge(self, value1, value2):
    """获取两个顶点的关系"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')

    return self.vertices[value1].edges.get(self.vertices[value2])

  def deleteVertex(self, value):
    """删除顶点"""
    if value not in self.vertices:
      raise ValueError('顶点不存在')
    thisVertex = self.vertices[value]
    for vertex in thisVertex.edges:
      vertex.edges.pop(thisVertex)
    return self.vertices.pop(value)

  def deleteEdge(self, value1, value2):
    """删除关系"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')
    self.vertices[value1].edges.pop(self.vertices[value2])
    return self.vertices[value2].edges.pop(self.vertices[value1])

  def getNeighbors(self, value):
    """获取与该顶点有关的元素"""
    if value not in self.vertices:
      raise ValueError('顶点不存在')
    return [vertex.value for vertex in self.vertices[value].edges.keys()]


class SingleRelationGraph:
  """
  单向关系图/邻接表

  适用于频繁增删改查
  """

  class _SingleRelationVertex:
    """
    顶点
    """

    def __init__(self, value):
      self.value = value
      self.edges = dict()

    def addEdge(self, other: "SingleRelationGraph._SingleRelationVertex", weight):
      self.edges[other] = weight

  def __init__(self):
    self.vertices = dict()

  def addVertex(self, value):
    """添加顶点元素"""
    if value in self.vertices:
      raise ValueError('顶点已存在')
    self.vertices[value] = SingleRelationGraph._SingleRelationVertex(value)

  def addEdge(self, value1, value2, weight):
    """添加顶点之间的关系，value1指向value2的关系"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')
    self.vertices[value1].addEdge(self.vertices[value2], weight)

  def getEdge(self, value1, value2):
    """获取两个顶点之间的关系，value1指向value2的关系"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')
    return self.vertices[value1].edges.get(self.vertices[value2])

  def deleteVertex(self, value):
    """删除顶点"""
    if value not in self.vertices:
      raise ValueError('顶点不存在')
    thisVertex = self.vertices[value]
    for vertex in thisVertex.edges:
      vertex.edges.pop(thisVertex)
    return self.vertices.pop(value)

  def deleteEdge(self, value1, value2):
    """删除关系"""
    if value1 not in self.vertices or value2 not in self.vertices:
      raise ValueError('顶点不存在')
    return self.vertices[value1].edges.pop(self.vertices[value2])

  def getPointIn(self, value):
    """获取该顶点指向的元素"""
    if value not in self.vertices:
      raise ValueError('顶点不存在')
    return [vertex.value for vertex in self.vertices[value].edges.keys()]


if __name__ == '__main__':
  # graph = DoubleRelationGraph()
  graph = SingleRelationGraph()
  graph.addVertex("me")
  graph.addVertex("father")
  graph.addVertex("mother")
  graph.addVertex("grandfather")
  graph.addVertex("lily")
  graph.addVertex("boss")
  graph.addVertex("alex")

  graph.addEdge("me", "father", "dad-son")
  graph.addEdge("me", "mother", "mom-son")
  graph.addEdge("me", "grandfather", "pa-son")
  graph.addEdge("mother", "father", "couple")
  graph.addEdge("father", "grandfather", "dad-son")
  graph.addEdge("mother", "lily", "bestfriend")
  graph.addEdge("father", "boss", "employee-boss")
  graph.addEdge("lily", "alex", "friend")
  graph.addEdge("grandfather", "alex", "teacher-student")
  graph.addEdge("alex", "boss", "couple")

  print(graph.getEdge("me", "father"))
  # print(graph.getNeighbors("father"))
  print(graph.getPointIn("father"))
