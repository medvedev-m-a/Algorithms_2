class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def __str__(self):
        return f"TreeNode({self.NodeKey} - {self.NodeValue})"


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None
        self.CurrentInit()
        if self.Root:
            self.count = 1
        else:
            self.count = 0

    def PrintTree(self, node):
        if node is None:
            node = self.Root
        if node.LeftChild:
            self.PrintTree(node.LeftChild)
        print(node)
        if node.RightChild:
            self.PrintTree(node.RightChild)

    def CurrentInit(self):
        self.currentNode = BSTFind()
        self.currentNode.Node = self.Root

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу

        # если дерево пустое, результат None
        if self.Root is None:
            return None

        # проверка NodeKey == key
        if self.currentNode.Node.NodeKey == key:
            self.currentNode.NodeHasKey = True
            # print(self.currentNode.Node.NodeKey, self.currentNode.NodeHasKey, self.currentNode.ToLeft)
            return self.currentNode

        # проверка NodeKey < key
        if self.currentNode.Node.NodeKey > key:
            if self.currentNode.Node.LeftChild is None:
                self.currentNode.ToLeft = True
                # print(self.currentNode.Node.NodeKey, self.currentNode.NodeHasKey, self.currentNode.ToLeft)
                return self.currentNode
            self.currentNode.Node = self.currentNode.Node.LeftChild

        # проверка NodeKey > key
        if self.currentNode.Node.NodeKey < key:
            if self.currentNode.Node.RightChild is None:
                # print(self.currentNode.Node.NodeKey, self.currentNode.NodeHasKey, self.currentNode.ToLeft)
                return self.currentNode
            self.currentNode.Node = self.currentNode.Node.RightChild

        # рекурсивно запускаем FindNodeByKey
        return self.FindNodeByKey(key)

    def AddKeyValue(self, key, val):
        self.CurrentInit()
        # добавляем ключ-значение в дерево
        if self.FindNodeByKey(key).NodeHasKey:
            return False  # если ключ уже есть
        self.newNode = BSTNode(key, val, self.currentNode.Node)
        if self.currentNode.ToLeft:
            self.currentNode.Node.LeftChild = self.newNode
        else:
            self.currentNode.Node.RightChild = self.newNode
        self.count += 1
        self.CurrentInit()

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FindMax is True:
            if FromNode.RightChild is None:
                # print(FromNode)
                return FromNode
            FromNode = FromNode.RightChild
        elif FindMax is False:
            if FromNode.LeftChild is None:
                # print(FromNode)
                return FromNode
            FromNode = FromNode.LeftChild

        return self.FinMinMax(FromNode, FindMax)

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        # ищем узел ко ключу
        self.CurrentInit()

        # если узел не найден, возвращаем False
        if self.FindNodeByKey(key).NodeHasKey is False:
            return False  # если узел не найден

        self.nodeToDelete = self.FindNodeByKey(key).Node
        self.nodeToReplace = self.childLeftOrRight(self.nodeToDelete)

        self.parentLeftOrRight(self.nodeToDelete, self.nodeToReplace)
        self.count -= 1

    def parentLeftOrRight(self, nodeToDelete, nodeToReplace):
        if nodeToDelete.Parent.LeftChild == nodeToDelete:
            nodeToDelete.Parent.LeftChild = nodeToReplace
        elif nodeToDelete.Parent.RightChild == nodeToDelete:
            nodeToDelete.Parent.RightChild = nodeToReplace
        nodeToDelete.Parent = nodeToReplace
        return None

    def childLeftOrRight(self, nodeToDelete):
        if nodeToDelete.LeftChild is None and nodeToDelete.RightChild is None:
            return None
        elif nodeToDelete.LeftChild and nodeToDelete.RightChild is None:
            return nodeToDelete.LeftChild
        elif nodeToDelete.LeftChild is None and nodeToDelete.RightChild:
            return nodeToDelete.RightChild
        else:
            self.minRight = self.FinMinMax(nodeToDelete.RightChild, False)
            self.minRight.LeftChild = nodeToDelete.LeftChild
            nodeToDelete.LeftChild.Parent = self.minRight
            return self.minRight

    def Count(self):
        return self.count  # количество узлов в дереве
