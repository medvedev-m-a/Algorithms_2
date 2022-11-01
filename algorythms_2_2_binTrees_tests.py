from algorythms_2_2_binTrees import BSTNode, BST

nodes = [64, 21, 99, 57, 90, 163, 34, 59, 103, 171, 36, 62, 143, 182]
tree = BST(BSTNode(nodes[0], 0, None))

# tree.PrintTree(None)
# print(tree.Count())
# print()

# tree.DeleteNodeByKey(nodes[0])
#
# tree.PrintTree(None)
# print(tree.Count())
# print()

for i in range(1, 14):  # len(nodes)):
    tree.AddKeyValue(nodes[i], i)

tree.PrintTree(None)
print(tree.Count())
print()

for i in range(13):  # len(nodes)):
    tree.DeleteNodeByKey(nodes[i])

tree.DeleteNodeByKey(nodes[0])

tree.PrintTree(None)
print(tree.Count())
print()

