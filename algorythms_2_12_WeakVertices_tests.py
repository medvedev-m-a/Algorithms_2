from algorythms_2_12_WeakVertices import *
# import unittest
# import random
#
#
# class MyTests(unittest.TestCase):
#
#     def test_DepthFirstSearch(self):
#         size = 5
#         sg = SimpleGraph(size)
#
#         for _ in range(size):
#             sg.AddVertex(_)
#
#         sg.AddEdge(0, 1)
#         sg.AddEdge(0, 2)
#         sg.AddEdge(0, 3)
#         sg.AddEdge(1, 3)
#         sg.AddEdge(1, 4)
#         sg.AddEdge(2, 3)
#         sg.AddEdge(3, 4)
#         sg.AddEdge(3, 3)
#
#         print(sg.m_adjacency)
#
#         print(sg.DepthFirstSearch(0, 4))
#
#         # self.assertEqual(sg.IsEdge(v1, v2), True)
#         # self.assertEqual(sg.IsEdge(v2, v1), True)
#         # self.assertEqual(sg.IsEdge(v1 + 1, v2), False)
#
#
# if __name__ == '__main__':
#     unittest.main()

size = 8
sg = SimpleGraph(size)

for _ in range(size):
    sg.AddVertex(_)

sg.AddEdge(0, 2)
sg.AddEdge(1, 3)
sg.AddEdge(3, 4)
sg.AddEdge(3, 2)
sg.AddEdge(3, 5)
sg.AddEdge(3, 6)
sg.AddEdge(3, 7)
sg.AddEdge(2, 6)
sg.AddEdge(4, 5)

print(sg.m_adjacency)

lll = sg.WeakVertices()
for i in lll:
    print(i, end='-> ')
