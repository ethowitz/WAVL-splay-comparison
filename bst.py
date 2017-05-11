class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root:
            self._insert(key, self.root)
        else:
            self.root = Node(key)

    def _insert(self, key, node):
        if key < node.key:
            if node.left:
                self._insert(key, node.left)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = Node(key)

    def remove(self, key):
        pass

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0

        lheight = self._height(node.left)
        rheight = self._height(node.right)
        return max(lheight, rheight) + 1

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if not node:
            return False
        elif key == node.key:
            return True
        elif key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)
