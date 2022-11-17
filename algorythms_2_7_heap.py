class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    # def __str__(self) -> str:
    #     return f'{self.HeapArray}'

    def MakeHeap(self, a: list, depth: int) -> None:
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        self.HeapArray = [-1] * (2 ** (depth + 1) - 1)
        for key in a:
            if self.Add(key):
                continue
            break

    def GetMax(self) -> int:
        # вернуть значение корня и перестроить кучу
        if self.HeapArray[0] < 0:
            return -1  # если куча пуста
        # извлекаем корень
        root: int = self.HeapArray.pop(0)

        # меняем местами последний узел с корневым
        last_index = self.last_item_index()
        self.HeapArray.insert(0, self.HeapArray[last_index])
        self.HeapArray[last_index + 1] = -1

        # перестраиваем кучу
        self.rebuild_heap(0)

        return root

    def Add(self, key: int) -> bool:
        # добавляем новый элемент key в кучу и перестраиваем её
        if key < 0:
            return False

        # ищем индекс последнего свободного слота
        last_empty_index = self.last_item_index() + 1

        # проверка на заполненность кучи
        if last_empty_index > len(self.HeapArray):
            return False  # если куча вся заполнена

        self.HeapArray[last_empty_index] = key
        self.rebuild_heap(last_empty_index)
        return True

    def rebuild_heap(self, ind: int) -> None:
        parent = 0
        max_child = -1

        if ind > 0:
            parent = (ind - 1) // 2

        if 2 * ind + 1 < len(self.HeapArray):
            if self.HeapArray[2 * ind + 1] >= self.HeapArray[2 * ind + 2]:
                max_child = 2 * ind + 1
            else:
                max_child = 2 * ind + 2

        if self.HeapArray[parent] >= self.HeapArray[ind] > self.HeapArray[max_child]:
            return None
        elif self.HeapArray[ind] < self.HeapArray[max_child]:
            self.HeapArray[ind], self.HeapArray[max_child] = self.HeapArray[max_child], self.HeapArray[ind]
            ind = max_child
        elif self.HeapArray[parent] < self.HeapArray[ind]:
            self.HeapArray[ind], self.HeapArray[parent] = self.HeapArray[parent], self.HeapArray[ind]
            ind = parent
        return self.rebuild_heap(ind)

    def last_item_index(self) -> int:
        for i in range(len(self.HeapArray) - 1, -1, -1):
            if self.HeapArray[i] >= 0:
                return i
        return -1
