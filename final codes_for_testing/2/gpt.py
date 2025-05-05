import unittest
from c import Tree, Node
class TestBinarySearchTree(unittest.TestCase):

    def test_insert(self):
        bst = Tree()
        bst.insert(5)
        self.assertTrue(bst.search(5))

    def test_search(self):
        bst = Tree()
        bst.insert(5)
        self.assertTrue(bst.search(5))
        self.assertFalse(bst.search(10))

    def test_remove_leaf_node(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.remove(3)
        self.assertFalse(bst.search(3))

    def test_remove_node_with_one_child(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.remove(3)
        self.assertFalse(bst.search(3))
        self.assertTrue(bst.search(7))

    def test_remove_node_with_two_children(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(6)
        bst.remove(7)
        self.assertFalse(bst.search(7))
        self.assertTrue(bst.search(6))

    def test_inorder_traversal(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.inorder(), [3, 5, 7])

if __name__ == '__main__':
    unittest.main()