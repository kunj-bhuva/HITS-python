import unittest
from c import Graph, Vertex
class TestVertex(unittest.TestCase):
    def test_init_valid_input(self):
        v = Vertex("A")
        self.assertEqual(v.name, "A")
        self.assertEqual(v.neighbors, [])
        self.assertEqual(v.discovery, 0)
        self.assertEqual(v.finish, 0)
        self.assertEqual(v.color, 'black')

    def test_init_long_input(self):
        v = Vertex("Vertex1")
        self.assertEqual(v.name, "Vertex1")
        self.assertEqual(v.neighbors, [])
        self.assertEqual(v.discovery, 0)
        self.assertEqual(v.finish, 0)
        self.assertEqual(v.color, 'black')

    def test_init_special_character_input(self):
        v = Vertex("@")
        self.assertEqual(v.name, "@")
        self.assertEqual(v.neighbors, [])
        self.assertEqual(v.discovery, 0)
        self.assertEqual(v.finish, 0)
        self.assertEqual(v.color, 'black')

    def test_init_empty_input(self):
        v = Vertex("")
        self.assertEqual(v.name, "")
        self.assertEqual(v.neighbors, [])
        self.assertEqual(v.discovery, 0)
        self.assertEqual(v.finish, 0)
        self.assertEqual(v.color, 'black')

    def test_add_neighbor_not_exist(self):
        v = Vertex("A")
        v.add_neighbor("B")
        self.assertEqual(v.neighbors, ["B"])

    def test_add_neighbor_already_exist(self):
        v = Vertex("A")
        v.neighbors = ["B"]
        v.add_neighbor("B")
        self.assertEqual(v.neighbors, ["B"])

    def test_add_neighbor_empty_list(self):
        v = Vertex("A")
        v.add_neighbor("C")
        self.assertEqual(v.neighbors, ["C"])

    def test_add_neighbor_multiple_neighbors(self):
        v = Vertex("A")
        v.neighbors = ["B"]
        v.add_neighbor("D")
        self.assertEqual(v.neighbors, ["B", "D"])

    def test_add_neighbor_different_data_type(self):
        v = Vertex("A")
        with self.assertRaises(TypeError):
            v.add_neighbor(1)

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

    def test_add_vertex_valid_input(self):
        self.assertTrue(self.graph.add_vertex(Vertex('D')))
        self.assertFalse(self.graph.add_vertex(Vertex('A')))

    def test_add_vertex_invalid_input(self):
        self.assertFalse(self.graph.add_vertex("A"))

    def test_add_edge_valid_input(self):
        self.assertTrue(self.graph.add_edge('B', 'C'))
        self.assertFalse(self.graph.add_edge('A', 'D'))

    def test_add_edge_invalid_input(self):
        self.assertFalse(self.graph.add_edge('E', 'F'))

    def test_get_vertex_existing_vertex(self):
        self.assertEqual(self.graph.get_vertex('A'), self.vertex1)

    def test_get_vertex_non_existing_vertex(self):
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