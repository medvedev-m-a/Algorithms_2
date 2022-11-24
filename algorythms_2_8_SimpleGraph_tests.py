from algorythms_2_8_SimpleGraph import *
import unittest
import random


class MyTests(unittest.TestCase):

    def test_add_vertex(self):
        size = 5
        findings = []
        for _ in range(size+10):
            findings.append(_ * 100)
        sg = SimpleGraph(size)
        for _ in range(size):
            self.assertEqual(sg.IsVertex(findings[_]), False)

        for _ in range(size+10):
            sg.AddVertex(findings[_])

        for _ in range(size):
            self.assertEqual(sg.IsVertex(findings[_]), True)

    def test_add_edge(self):
        size = 8
        findings = []
        sg = SimpleGraph(size)
        v1 = random.randint(0, size-1)
        v2 = random.randint(0, size-1)

        for _ in range(size+10):
            findings.append(_ * 100)
            sg.AddVertex(findings[_])

        self.assertEqual(sg.IsEdge(v1, v2), False)

        sg.AddEdge(v1, v2)

        self.assertEqual(sg.IsEdge(v1, v2), True)
        self.assertEqual(sg.IsEdge(v2, v1), True)
        self.assertEqual(sg.IsEdge(v1 + 1, v2), False)

    def test_remove_edge(self):
        size = 8
        findings = []
        sg = SimpleGraph(size)
        v1 = random.randint(0, size-1)
        v2 = random.randint(0, size-1)

        for _ in range(size+10):
            findings.append(_ * 100)
            sg.AddVertex(findings[_])

        self.assertEqual(sg.IsEdge(v1, v2), False)

        sg.AddEdge(v1, v2)

        self.assertEqual(sg.IsEdge(v1, v2), True)
        self.assertEqual(sg.IsEdge(v2, v1), True)
        self.assertEqual(sg.IsEdge(v1 + 1, v2), False)

        sg.RemoveEdge(v1, v2)

        self.assertEqual(sg.IsEdge(v1, v2), False)

    def test_remove_vertex(self):
        size = 8
        sg = SimpleGraph(size)

        v1 = random.randint(0, size-1)
        v2 = random.randint(0, size-1)
        for _ in range(size*10):
            v3 = random.randint(0, size-1)
            if v3 != v1 and v3 != v2:
                break

        for _ in range(size+10):
            sg.AddVertex(_ * 100)

        sg.AddEdge(v1, v2)

        self.assertEqual(sg.IsEdge(v1, v2), True)
        self.assertEqual(sg.IsEdge(v2, v1), True)
        self.assertEqual(sg.IsEdge(v3, v2), False)
        self.assertEqual(sg.IsEdge(v3, v1), False)

        sg.RemoveVertex(v1)

        for _ in range(size):
            self.assertEqual(sg.IsEdge(v1, _), False)


if __name__ == '__main__':
    unittest.main()
