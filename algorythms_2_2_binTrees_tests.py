from algorythms_2_2_binTrees import BSTNode, BST

# a1 = BSTNode(50, 50, None)
# a2 = BSTNode(40, 40, a1)
# a5 = BSTNode(60, 60, a1)
#
# a1.LeftChild = a2
# a1.RightChild = a5
#
# tree = BST(a1)
#
# tree.FindNodeByKey(20)
#
# tree.AddKeyValue(20, 20)
# tree.AddKeyValue(20, 20)
# tree.AddKeyValue(30, 30)
# tree.AddKeyValue(70, 70)
# tree.AddKeyValue(45, 45)
#
#
# tree.FindNodeByKey(70)
#
# tree.FinMinMax(a1, False)
#
# tree.AddKeyValue(46, 46)
#
# tree.PrintTree(None)
# print()
#
# tree.DeleteNodeByKey(50)
#
# tree.PrintTree(None)
#
a1 = BSTNode(182,0,None)
tree = BST(a1)
tree.AddKeyValue(78,0)
tree.AddKeyValue(185,0)
tree.AddKeyValue(60,0)
tree.AddKeyValue(91,0)
tree.AddKeyValue(192,0)
tree.AddKeyValue(10,0)
tree.AddKeyValue(68,0)
tree.AddKeyValue(133,0)
tree.AddKeyValue(9,0)
tree.AddKeyValue(60,0)
tree.AddKeyValue(63,0)
tree.AddKeyValue(124,0)
tree.AddKeyValue(139,0)

tree.PrintTree(None)
print(tree.Count())

tree.DeleteNodeByKey(182)
# tree.DeleteNodeByKey(175)
# tree.DeleteNodeByKey(123)


tree.PrintTree(None)
print(tree.Count())
