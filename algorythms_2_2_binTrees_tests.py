import unittest
import random
from algorythms_2_2_binTrees import BSTNode, BST


class MyTests(unittest.TestCase):

    # seria of empty tests
    def test_delete_root(self):
        nodes = [64, 21, 99, 57, 90, 163, 34, 59, 103, 171, 36, 62, 143, 182]
        tree = BST(None)
        for i in range(5):
            tree.AddKeyValue(nodes[i], nodes[i] * 10)

        for i in range(5):
            par_test = False
            nod = tree.FindNodeByKey(nodes[i]).Node
            par = nod.Parent
            if par.LeftChild == nod or par.RightChild == nod:
                par_test = True
            self.assertEqual(par_test, True)

            self.assertEqual(tree.DeleteNodeByKey(nodes[i]), None)
            if par.LeftChild != nod and par.RightChild != nod:
                par_test = False
            self.assertEqual(par_test, False)

        for i in range(1, 5):
            self.assertEqual(tree.DeleteNodeByKey(nodes[i]), False)


if __name__ == '__main__':
    unittest.main()


# tree.PrintTree(None)
# print(tree.Count())
# print()

# tree.DeleteNodeByKey(nodes[0])
#
# tree.PrintTree(None)
# print(tree.Count())
# print()

# for i in range(1, 5):  # len(nodes)):
#     tree.AddKeyValue(nodes[i], i)
#
# tree.PrintTree(None)
# print(tree.Count())
# print()

# for i in range(2):  # len(nodes)):
#     tree.DeleteNodeByKey(nodes[i])

# tree.DeleteNodeByKey(nodes[4])
#
# tree.PrintTree(None)
# print(tree.Count())
# print()

