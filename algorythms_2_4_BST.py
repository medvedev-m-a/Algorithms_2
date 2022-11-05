class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * self.tree_size  # массив ключей
        self.not_null = False

    def __str__(self):
        return f'{self.Tree}'

    def FindKeyIndex(self, key) -> int:
        # ищем в массиве индекс ключа
        key_index: int = 0
        return self.FindKey(key, key_index)

    def FindKey(self, key, key_index: int) -> int:
        # индекс его родителя: (I - 1) / 2
        # Индекс левого потомка: 2 * I + 1
        # Индекс правого потомка: 2 * I + 2

        # если массив пустой
        if self.not_null is False:
            return 0

        # если массивт заполнен, но узел не найден
        if key_index > self.tree_size:
            return None

        # если индекс сообвествует, но ключ пустой
        # либо сравниваем ключ на равенство
        if self.Tree[key_index] is None:
            return -key_index

        elif self.Tree[key_index] == key:
            return key_index

        elif self.Tree[key_index] > key:
            key_index = 2 * key_index + 1
            return self.FindKey(key, key_index)

        elif self.Tree[key_index] < key:
            key_index = 2 * key_index + 2
            return self.FindKey(key, key_index)

    def AddKey(self, key) -> int:
        # добавляем ключ в массив
        find_index = self.FindKeyIndex(key)

        # индекс добавленного/существующего ключа или -1 если не удалось
        if find_index is None:
            return -1

        # если узел найден, но ключ пустой, добавляем ключ
        elif find_index <= 0:
            self.Tree[-find_index] = key
            self.not_null = True
            find_index = -find_index

        return find_index
