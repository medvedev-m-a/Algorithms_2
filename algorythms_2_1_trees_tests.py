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

tree.AddChild(a1, a3)

tree.AddChild(a2, a4)
tree.AddChild(a2, a5)
tree.AddChild(a3, a6)


tree.AddChild(a5, a7)

tree.AddChild(a7, a8)
print(tree.GetAllNodes(), tree.Count())
for _ in tree.GetAllNodes():
    print(_)

tree.DeleteNode(a3)
print(tree.GetAllNodes(), tree.Count())
for _ in tree.GetAllNodes():
    print(_)
