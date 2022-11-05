from algorythms_2_4_BST import *

tree = aBST(4)
nodes = [64, 20, 90, 25, 85, 95, 10, 17, 22, 27, 82, 87, 92, 97]
# print(tree)
for i in range(len(nodes)):
    print(tree.AddKey(nodes[i]))
print(tree)

for i in range(len(nodes)):
    print(tree.FindKeyIndex(nodes[i]))
