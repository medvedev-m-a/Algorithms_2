class Vertex:

    def __init__(self, val: int) -> None:
        self.Value = val


class SimpleGraph:

    def __init__(self, size: int) -> None:
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v: int) -> None:
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex.insert(i, Vertex(v))
                return None

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v: int) -> None:
        # ваш код удаления вершины со всеми её рёбрами
        if 0 <= v <= self.max_vertex - 1:
            self.vertex[v] = None
            for i in range(self.max_vertex):
                self.m_adjacency[i][v] = self.m_adjacency[v][i] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        if 0 <= v1 <= self.max_vertex - 1 and 0 <= v2 <= self.max_vertex - 1:
            if self.m_adjacency[v1][v2]:
                return True
            return False

    def AddEdge(self, v1: int, v2: int) -> None:
        # добавление ребра между вершинами v1 и v2
        if 0 <= v1 <= self.max_vertex - 1 and 0 <= v2 <= self.max_vertex - 1:
            self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        # удаление ребра между вершинами v1 и v2
        if 0 <= v1 <= self.max_vertex - 1 and 0 <= v2 <= self.max_vertex - 1:
            self.m_adjacency[v1][v2] = self.m_adjacency[v2][v1] = 0

    def IsVertex(self, val: int) -> bool:
        for i in range(self.max_vertex):
            if isinstance(self.vertex[i], Vertex) and self.vertex[i].Value == val:
                return True
        return False
