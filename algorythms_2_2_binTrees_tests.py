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
a1 = BSTNode(123,123,None)
tree = BST(a1)
tree.AddKeyValue(98,98)
tree.AddKeyValue(136,136)
tree.AddKeyValue(93,93)
tree.AddKeyValue(119,119)
tree.AddKeyValue(164,164)
tree.AddKeyValue(4,4)
tree.AddKeyValue(121,121)
tree.AddKeyValue(139,139)
tree.AddKeyValue(175,175)
tree.AddKeyValue(3,3)
tree.AddKeyValue(86,86)
tree.AddKeyValue(163,163)
tree.AddKeyValue(178,178)

tree.PrintTree(None)
print(tree.Count())

tree.DeleteNodeByKey(98)
tree.DeleteNodeByKey(175)
tree.DeleteNodeByKey(4)


tree.PrintTree(None)
print(tree.Count())
