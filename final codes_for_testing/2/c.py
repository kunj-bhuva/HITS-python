


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def remove(self, val):
        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._remove(node.left, val)
        elif val > node.val:
            node.right = self._remove(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.val = min_larger_node.val
            node.right = self._remove(node.right, min_larger_node.val)
        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

if __name__ == "__main__":
    import sys
    bst = Tree()

    n = int(sys.stdin.readline())
    for _ in range(n):
        parts = sys.stdin.readline().strip().split()
        if not parts:
            continue
        cmd = parts[0].lower()
        if cmd == "insert" and len(parts) == 2:
            bst.insert(int(parts[1]))
        elif cmd == "search" and len(parts) == 2:
            found = bst.search(int(parts[1]))
            print("Found" if found else "Not found")
        elif cmd == "delete" and len(parts) == 2:
            bst.remove(int(parts[1]))
        elif cmd == "inorder":
            print("Inorder:", bst.inorder())

      