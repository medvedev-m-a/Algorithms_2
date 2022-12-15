class Vertex:

    def __init__(self, val: int) -> None:
        self.Value = val
        self.Hit = False
        self.bfs_parent = None

    def __str__(self):
        return f"TreeNode({self.Value})"


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.size() != 0:
            return self.queue.pop()

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() != 0:
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
        if 0 > v or v > self.max_vertex - 1:
            return None
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = self.m_adjacency[v][i] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        if 0 <= v1 <= self.max_vertex - 1 and 0 <= v2 <= self.max_vertex - 1:
            return self.m_adjacency[v1][v2]

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
            if self.IsEdge(VCurrent, Vmid) and self.vertex[Vmid].Hit is False:
                self.vertex[Vmid].Hit = True
                dfs_stack.push(Vmid)
                return self.dfs_search(Vmid, VTo, dfs_stack)

        # 5) Если непосещённых смежных вершин более нету, удаляем из стека верхний элемент.
        # Если стек пуст, то прекращаем работу и информируем, что путь не найден.
        # В противном случае делаем текущей вершиной X верхний элемент стека,
        # помечаем его как посещённый, и после чего переходим к п. 4.
        dfs_stack.pop()
        if dfs_stack.peek() is None:
            return []

        self.vertex[dfs_stack.peek()].Hit = True
        return self.dfs_search(dfs_stack.peek(), VTo, dfs_stack)

    def stack_to_vertexlist(self, stack: Stack) -> list:
        vertexlist = []
        for i in stack.stack:
            if self.vertex[i]:
                vertexlist.insert(0, self.vertex[i])
        return vertexlist

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> list:
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        bfs_queue = Queue()
        self.clean()

        # 1) Выбираем текущую вершину X. Для начала работы это будет исходная вершина А.
        # Фиксируем вершину А как посещённую.
        self.vertex[VFrom].Hit = True

        return self.bfs_search(VFrom, VTo, bfs_queue)

    def bfs_search(self, VCurrent: int, VTo: int, bfs_queue: Queue) -> list:
        path = []

        # 2) Из всех смежных с X вершин выбираем любую (например первую) непосещённую.
        for Vmid in range(self.max_vertex):
            if self.IsEdge(VCurrent, Vmid) and self.vertex[Vmid].Hit is False:
                self.vertex[Vmid].bfs_parent = VCurrent
                self.vertex[Vmid].Hit = True

                # Если выбранная вершина равна искомой, значит цель найдена,
                # заканчиваем работу (остаётся только сформировать до неё путь,
                # если это требуется).
                if Vmid == VTo:
                    return self.bfs_path(VTo, path)

                bfs_queue.enqueue(Vmid)

        # Если таких вершин нету, проверяем очередь:
        # Если очередь пуста, заканчиваем работу (путь до цели не найден).
        # Иначе извлекаем из очереди очередной элемент, делаем его текущим X,
        # и переходим обратно к данному п.2.
        if bfs_queue.size() == 0:
            return []

        return self.bfs_search(bfs_queue.dequeue(), VTo, bfs_queue)

    def bfs_path(self, Vpath: int, path: list) -> list:
        path.insert(0, self.vertex[Vpath])
        if self.vertex[Vpath].bfs_parent is None:
            return path
        return self.bfs_path(self.vertex[Vpath].bfs_parent, path)

    def WeakVertices(self) -> list:
        # возвращает список узлов вне треугольников
        weak_list = []

        for v_current in range(self.max_vertex):
            check_list = []

            # формируем список смежных вершин
            for v in range(self.max_vertex):
                if self.m_adjacency[v_current][v] or self.m_adjacency[v][v_current]:
                    check_list.append(v)

            # формирование итогового списка
            if self.is_edge_in_list(check_list) is False:
                weak_list.append(self.vertex[v_current])

        return weak_list

    # проверка есть ли ребра у списка вершин
    def is_edge_in_list(self, check_list: list) -> bool:
        if len(check_list) < 2:
            return False

        for i in range(len(check_list) - 1):
            if self.IsEdge(check_list[i], check_list[i+1]):
                return True
        return False

    def clean(self) -> None:
        # очищаем параметры вершин графа
        for v in self.vertex:
            if v is not None:
                v.Hit = False
                v.bfs_parent = None
