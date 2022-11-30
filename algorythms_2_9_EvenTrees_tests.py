from algorythms_2_9_EvenTrees import *

a1 = SimpleTreeNode(1, None)
a2 = SimpleTreeNode(2, None)
a3 = SimpleTreeNode(3, None)
a4 = SimpleTreeNode(4, None)
a5 = SimpleTreeNode(5, None)
a6 = SimpleTreeNode(6, None)
a7 = SimpleTreeNode(7, None)
a8 = SimpleTreeNode(8, None)
a9 = SimpleTreeNode(9, None)
a10 = SimpleTreeNode(10, None)

tree = SimpleTree(a1)

tree.AddChild(a1, a2)
tree.AddChild(a1, a3)
tree.AddChild(a1, a6)

tree.AddChild(a2, a5)
tree.AddChild(a2, a7)

tree.AddChild(a3, a4)

tree.AddChild(a6, a8)
tree.AddChild(a8, a9)
tree.AddChild(a8, a10)


print(tree.GetAllNodes(), tree.Count())
for _ in tree.GetAllNodes():
    print(_)

dell = tree.EvenTrees()
print(dell)
