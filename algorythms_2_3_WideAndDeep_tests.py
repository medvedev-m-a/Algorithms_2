from algorythms_2_3_WideAndDeep import *

nodes = [64, 21, 99, 57, 90, 163, 34, 59, 103, 171, 36, 62, 143, 182]
a1 = BSTNode(nodes[0], nodes[0] * 10, None)
tree = BST(a1)
for i in range(1, 5):
    tree.AddKeyValue(nodes[i], nodes[i] * 10)

tree.PrintTree(a1)
# print()
n = tree.DeepAllNodes(2)
h = tree.WideAllNodes()
pass