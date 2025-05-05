import unittest
from c import Tree, Node
class TestBinarySearchTree(unittest.TestCase):

    def test_insert_positive_integer(self):
        bst = Tree()
        bst.insert(5)
        self.assertTrue(bst.search(5))

    def test_insert_negative_integer(self):
        bst = Tree()
        bst.insert(-10)
        self.assertTrue(bst.search(-10))

    def test_insert_zero(self):
        bst = Tree()
        bst.insert(0)
        self.assertTrue(bst.search(0))

    def test_insert_large_integer(self):
        bst = Tree()
        bst.insert(999999)
        self.assertTrue(bst.search(999999))

    def test_insert_non_integer_value(self):
        bst = Tree()
        with self.assertRaises(TypeError):
            bst.insert("abc")

    def test_insert_float_value(self):
        bst = Tree()
        with self.assertRaises(TypeError):
            bst.insert(3.14)

    def test_insert_empty_tree(self):
        bst = Tree()
        self.assertIsNone(bst.root)

    def test_insert_node_object(self):
        bst = Tree()
        node = Node(5)
        bst.root = node
        self.assertEqual(bst.root, node)

    def test_insert_invalid_input(self):
        bst = Tree()
        with self.assertRaises(TypeError):
            bst.insert([1, 2, 3])

    def test_search_existing_value(self):
        bst = Tree()
        bst.insert(5)
        self.assertTrue(bst.search(5))

    def test_search_non_existing_value(self):
        bst = Tree()
        bst.insert(5)
        self.assertFalse(bst.search(10))

    def test_remove_value_in_root_node(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        bst.remove(10)
        self.assertEqual(bst.inorder(), [12, 5, 15, 3, 7, 20])

    def test_remove_value_in_leaf_node(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        bst.remove(3)
        self.assertEqual(bst.inorder(), [10, 5, 15, 7, 12, 20])

    def test_remove_value_with_only_left_child(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        bst.remove(5)
        self.assertEqual(bst.inorder(), [10, 7, 15, 3, 12, 20])

    def test_remove_value_with_only_right_child(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        bst.remove(15)
        self.assertEqual(bst.inorder(), [10, 5, 20, 3, 7, 12])

    def test_remove_value_with_both_children(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        bst.remove(10)
        self.assertEqual(bst.inorder(), [12, 5, 15, 3, 7, 20])

    def test_get_min_single_node(self):
        bst = Tree()
        bst.insert(5)
        self.assertEqual(bst._get_min(bst.root).val, 5)

    def test_get_min_leftmost_leaf(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        self.assertEqual(bst._get_min(bst.root).val, 3)

    def test_get_min_rightmost_leaf(self):
        bst = Tree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(20)
        self.assertEqual(bst._get_min(bst.root.right).val, 12)

    def test_inorder_empty_tree(self):
        bst = Tree()
        self.assertEqual(bst.inorder(), [])

    def test_inorder_balanced_tree(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.inorder(), [3, 5, 7])

    def test_inorder_skewed_tree(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(2)
        self.assertEqual(bst.inorder(), [2, 3, 5])

    def test_inorder_duplicate_values(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(3)
        self.assertEqual(bst.inorder(), [3, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()