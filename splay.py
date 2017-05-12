import bst

class Splay(bst.BST):
    def __init__(self):
        super(Splay, self).__init__()

    def parent(self, x):
        if x:
            return x.parent
        else:
            return None

    def left(self, x):
        if x:
            return x.left
        else:
            return None

    def right(self, x):
        if x:
            return x.right
        else:
            return None

    def badsplay(self, x):
        assert x
        while self.parent(x):
            if x == self.left(self.parent(x)):
                if self.parent(x) == self.left(self.parent(self.parent(x))):
                    self.right_rotate(self.parent(self.parent(x)))
                self.right_rotate(self.parent(x))
            else:
                assert x == self.right(self.parent(x))
                if self.parent(x) == self.right(self.parent(self.parent(x))):
                    self.left_rotate(self.parent(self.parent(x)))
                self.left_rotate(self.parent(x))
            x = self.parent(x)

    def splay(self, x):
        while x != self.root:
            if x == x.parent.right:
                if x.parent == self.root:
                    self.left_rotate(x.parent)
                elif x.parent == x.parent.parent.right:
                    self.left_rotate(x.parent.parent)
                    self.left_rotate(x.parent)
                else:
                    assert x.parent == x.parent.parent.left
                    self.left_rotate(x.parent)
                    self.right_rotate(x.parent)
            else:
                assert x == x.parent.left
                if x.parent == self.root:
                    self.right_rotate(x.parent)
                elif x.parent == x.parent.parent.left:
                    self.right_rotate(x.parent.parent)
                    self.right_rotate(x.parent)
                else:
                    assert x.parent == x.parent.parent.right
                    self.right_rotate(x.parent)
                    self.left_rotate(x.parent)

    def insert(self, key):
        if self.root:
            self._insert(key, self.root)
        else:
            self.root = bst.Node(key)

    def _insert(self, key, node):
        if key < node.key:
            if node.left:
                self._insert(key, node.left)
            else:
                node.left = bst.Node(key, parent=node)
                self.splay(node.left)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = bst.Node(key, parent=node)
                self.splay(node.right)
