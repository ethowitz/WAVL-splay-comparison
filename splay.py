import bst

class Splay(bst.BST):
    def __init__(self):
        super(Splay, self).__init__()

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

    def _search(self, key, node):
        if not node:
            return False
        elif key == node.key:
            self.splay(node)
            return True
        elif key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    # adapted from CLRS edition 3, page 298
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
