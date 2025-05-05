import unittest
from c import Graph, Vertex
class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.vertex1 = Vertex('A')
        self.vertex2 = Vertex('B')
        self.vertex3 = Vertex('C')
        self.graph.add_vertex(self.vertex1)
        self.graph.add_vertex(self.vertex2)
        self.graph.add_vertex(self.vertex3)
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')

    def test_add_vertex(self):
        self.assertTrue(self.graph.add_vertex(Vertex('D')))
        self.assertFalse(self.graph.add_vertex(Vertex('A')))

    def test_add_edge(self):
        self.assertTrue(self.graph.add_edge('B', 'C'))
        self.assertFalse(self.graph.add_edge('A', 'D'))

    def test_get_vertex(self):
        self.assertEqual(self.graph.get_vertex('A'), self.vertex1)
        self.assertIsNone(self.graph.get_vertex('D'))

    def test_dfs(self):
        self.graph.dfs(self.vertex1)
        self.assertEqual(self.vertex1.discovery, 1)
        self.assertEqual(self.vertex1.finish, 6)
        self.assertEqual(self.vertex2.discovery, 2)
        self.assertEqual(self.vertex2.finish, 3)
        self.assertEqual(self.vertex3.discovery, 4)
        self.assertEqual(self.vertex3.finish, 5)

if __name__ == '__main__':
    unittest.main()