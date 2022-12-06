class Vertex:

    def __init__(self, val: int) -> None:
        self.Value = val
        self.Hit = False


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)
        return None

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[0]


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
                self.vertex[i] = Vertex(v)
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

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list:
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        # 0) Очищаем все дополнительные структуры данных: делаем стек пустым,
        # а все вершины графа отмечаем как непосещённые (см. далее).
        dfs_stack = Stack()
        for v in self.vertex:
            if v is not None:
                v.Hit = False

        # 1) Выбираем текущую вершину X. Для начала работы это будет исходная вершина А.
        VCurrent = VFrom
        self.vertex[VCurrent].Hit = True

        dfs_stack.push(VCurrent)


        return self.dfs_search(VCurrent, VTo, dfs_stack)

    def dfs_search(self, VCurrent: int, VTo: int, dfs_stack: Stack) -> list:
        # 2) Фиксируем вершину X как посещённую.
        # Для этого в класс Vertex надо добавить, например, флажок hit,
        # который принимает значение True, если вершина была таким образом посещёна.

        # 3) Помещаем вершину X в стек.

        # 4) Ищем среди смежных вершин вершины X целевую вершину Б.
        # Если она найдена, записываем её в стек и возвращаем сам стек
        # как результат работы (путь из А в Б).
        # Если целевой вершины среди смежных нету, то выбираем среди смежных
        # такую вершину, которая ещё не была посещена. Если такая вершина найдена,
        # делаем её текущей X и переходим к п. 2.
        if self.IsEdge(VCurrent, VTo):
            dfs_stack.push(VTo)
            return self.stack_to_vertexlist(dfs_stack)
        for Vmid in range(self.max_vertex):
            if self.IsEdge(VCurrent, Vmid):
                if self.vertex[Vmid].Hit is False:
                    self.vertex[Vmid].Hit = True
                    dfs_stack.push(Vmid)
                    return self.dfs_search(Vmid, VTo, dfs_stack)
                # 5) Если непосещённых смежных вершин более нету, удаляем из стека верхний элемент.
                # Если стек пуст, то прекращаем работу и информируем, что путь не найден.
                # В противном случае делаем текущей вершиной X верхний элемент стека,
                # помечаем его как посещённый, и после чего переходим к п. 4.
        # self.vertex[dfs_stack.pop()].Hit = False
        dfs_stack.pop()
        if dfs_stack.peek() is None:
            return []
        else:
            self.vertex[dfs_stack.peek()].Hit = True
            return self.dfs_search(dfs_stack.peek(), VTo, dfs_stack)

    def stack_to_vertexlist(self, stack: Stack) -> list:
        vertexlist =[]
        for i in stack.stack:
            if self.vertex[i]:
                vertexlist.insert(0, self.vertex[i])
        return vertexlist
