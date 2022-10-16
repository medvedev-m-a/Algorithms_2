from algorythms_2_1_trees import SimpleTree, SimpleTreeNode

a1 = SimpleTreeNode(9, None)
a2 = SimpleTreeNode(4, None)
a3 = SimpleTreeNode(17, None)
a4 = SimpleTreeNode(3, None)
a5 = SimpleTreeNode(6, None)
a6 = SimpleTreeNode(22, None)
a7 = SimpleTreeNode(5, None)
a8 = SimpleTreeNode(3, None)

tree = SimpleTree(a1)

tree.AddChild(a1, a2)
print(tree.LeafCount())

tree.AddChild(a1, a3)
print(tree.LeafCount())

tree.AddChild(a2, a4)
tree.AddChild(a2, a5)
tree.AddChild(a3, a6)
print(tree.LeafCount())


tree.AddChild(a5, a7)

all_nodes = tree.GetAllNodes()
print(all_nodes)
print(len(all_nodes))
print(tree.Count())

print(tree.FindNodesByValue(3))
tree.AddChild(a7, a8)
print(tree.FindNodesByValue(3))
tree.MoveNode(a7, a6)
print(tree.LeafCount())

print(a1)
print(a2)

tree.DeleteNode(a4)
