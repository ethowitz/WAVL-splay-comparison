class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.key = key
        self.parent = parent

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
                node.left = Node(key, parent=node)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = Node(key, parent=node)

    def get_node(self, key, node):
        if key == node.key:
            return node
        elif key < node.key:
            return self.get_node(key, node.left)
        else:
            return self.get_node(key, node.right)

    def remove(self, key):
        self._remove(self.get_node(key, self.root))

    # adapted from CLRS edition 3, page 296
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v != None:
            v.parent = u.parent

    def get_min(self, root):
        if root.left == None:
            return root
        else:
            return self.get_min(root.left)

    # addapted from CLRS edition 3, page 298
    def _remove(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.get_min(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

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
