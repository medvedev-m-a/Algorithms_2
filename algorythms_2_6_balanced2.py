class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a: list) -> None:
        # создаём дерево с нуля из неотсортированного массива a
        # сортируем массив a
        a.sort()
        self.recurcive_generate(self.Root, a)

    def IsBalanced(self, root_node: BSTNode) -> bool:
        # сбалансировано ли дерево с корнем root_node
        if root_node is None:
            root_node = self.Root
        left_leaf = self.FinMinMax(root_node, False).Level
        right_leaf = self.FinMinMax(root_node, True).Level
        if abs(left_leaf - right_leaf) <= 1:
            return True

        return False

    def FinMinMax(self, from_node, find_max):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if find_max is True:
            if from_node.RightChild is None:
                return from_node
            from_node = from_node.RightChild
        elif find_max is False:
            if from_node.LeftChild is None:
                return from_node
            from_node = from_node.LeftChild

        return self.FinMinMax(from_node, find_max)


    def recurcive_generate(self, root: BSTNode, array: list) -> BSTNode:
        if len(array) == 0:
            return root

        if root is None:
            self.Root = BSTNode(array[(len(array) - 1) // 2], None)
            root = self.Root
        else:
            if root.NodeKey > array[(len(array) - 1) // 2]:
                root.LeftChild = BSTNode(array[(len(array) - 1) // 2], root)
                root = root.LeftChild
            else:
                root.RightChild = BSTNode(array[(len(array) - 1) // 2], root)
                root = root.RightChild
            root.Level = root.Parent.Level + 1

        self.recurcive_generate(root, array[:(len(array) - 1) // 2])
        self.recurcive_generate(root, array[(len(array) - 1) // 2 + 1:])

    def GenerateBBSTArray(self, a: list) -> list:
        if len(a) == 0:
            return a

        # отсортировать массив а
        a.sort()
        node_que = [a]

        bst_array = []
        while node_que:
            curr = node_que.pop(0)
            root = (len(curr) - 1) // 2
            bst_array.append(curr[root])
            if len(curr) > 1:
                node_que.append(curr[:root])
                node_que.append(curr[root+1:])

        return bst_array
