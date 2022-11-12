from algorythms_2_6_balanced2 import *

nodes = [64, 20, 90, 25, 85, 95, 10, 17, 22, 27, 82, 87, 92, 97, 7]
# nodes = [64, 20, 90, 25, 85, 95, 82, 87, 92, 97, 99, 100, 102, 110, 111]

tree = BalancedBST()
print(tree.GenerateBBSTArray(nodes))
tree.GenerateTree(nodes)

print('tree balanced', tree.IsBalanced(None))
