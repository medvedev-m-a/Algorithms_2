class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def __str__(self):
        return f"TreeNode({self.NodeValue})"


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if self.Root is None:
            self.Root = NewChild
        else:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

        if NodeToDelete.Children:
            for Child in NodeToDelete.Children:
                self.DeleteNode(Child)

    def GetAllNodes(self):
        all_nodes = []
        if self.Root:
            self.GetAllChild(all_nodes, self.Root)
        return all_nodes

    def GetAllChild(self, all_nodes, node):
        all_nodes.append(node)
        if node.Children:
            for child in node.Children:
                self.GetAllChild(all_nodes, child)
        return all_nodes

    def FindNodesByValue(self, val):
        found_nodes = []
        if self.Root:
            self.FindValue(found_nodes, val, self.Root)
        return found_nodes

    def FindValue(self, found_nodes, val, node):
        if node.NodeValue == val:
            found_nodes.append(node)
        if node.Children:
            for child in node.Children:
                self.FindValue(found_nodes, val, child)
        return found_nodes

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode == self.Root:
            return
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        all_leaf = []
        if self.Root:
            self.FindLeafs(all_leaf, self.Root)
        return len(all_leaf)

    def FindLeafs(self, all_leaf, node):
        if node.Children:
            for child in node.Children:
                self.FindLeafs(all_leaf, child)
        else:
            all_leaf.append(node)
        return all_leaf
