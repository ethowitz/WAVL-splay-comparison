import bst

class WAVLNode(bst.Node):
    def __init__(self, key, left=None, right=None, rank=0, parent=None):
        super(WAVLNode, self).__init__(key, left, right)
        self.rank = rank
        self.parent = parent

class WAVL(bst.BST):
    def __init__(self):
        super(WAVL, self).__init__()

    def left_rotate(self, node):
        print("rotating!")
        # can't rotate at the root
        assert node.parent != None
        temp = node.left
        node.parent.right = temp
        node.left = node.parent

        if node.parent == self.root:
            self.root = node
        elif node.parent.parent.left == node.parent:
            node.parent.parent.left = node
        elif node.parent.parent.right == node.parent:
            node.parent.parent.right = node
        else:
            print("this can't happen")

    def right_rotate(self, node):
        print("rotating!")
        # can't rotate at the root
        assert node.parent != None
        temp = node.right
        node.parent.left = temp
        node.right = node.parent

        if node.parent == self.root:
            self.root = node
        elif node.parent.parent.left == node.parent:
            node.parent.parent.left = node
        elif node.parent.parent.right == node.parent:
            node.parent.parent.right = node
        else:
            print("this can't happen")

    def rank_diffs(self, node):
        assert node != None
        ldiff = node.rank + 1
        rdiff = node.rank + 1
        if node.left:
            ldiff = node.rank - node.left.rank
            assert ldiff >= 0
        if node.right:
            rdiff = node.rank - node.right.rank
            assert rdiff >= 0

        return (ldiff, rdiff)

    def promote(self, node):
        assert node != None
        node.rank += 1

    def demote(self, node):
        assert node != None
        node.rank -= 1

    def rebalance(self, node):
        parent_diffs = self.rank_diffs(node.parent)
        if parent_diffs == (0, 1) or parent_diffs == (1, 0):
            curr_node = node
            while curr_node.parent and (self.rank_diffs(curr_node.parent) == (0, 1) or self.rank_diffs(curr_node.parent) == (1, 0)):
                self.promote(curr_node.parent)
                curr_node = curr_node.parent

            if curr_node.parent and (self.rank_diffs(curr_node.parent) == (0, 2) or self.rank_diffs(curr_node.parent) == (2, 0)):
                if curr_node == curr_node.parent.left:
                    z = curr_node.parent
                    y = curr_node.right
                    if not y or curr_node.rank - y.rank == 2:
                        self.right_rotate(curr_node)
                        self.demote(z)
                    else:
                        self.rotate_left(y)
                        self.rotate_right(y)
                        self.promote(y)
                        self.demote(curr_node)
                        self.demote(z)
                else:
                    assert curr_node == curr_node.parent.right
                    z = curr_node.parent
                    y = curr_node.left
                    if not y or curr_node.rank - y.rank == 2:
                        self.left_rotate(curr_node)
                        self.demote(z)
                    else:
                        self.rotate_right(y)
                        self.rotate_left(y)
                        self.promote(y)
                        self.demote(curr_node)
                        self.demote(z)
        else:
            assert parent_diffs == (1, 1)

    def insert(self, key):
        if self.root:
            self._insert(key, self.root)
        else:
            self.root = WAVLNode(key)

    def _insert(self, key, node):
        if key < node.key:
            if node.left:
                self._insert(key, node.left)
            else:
                node.left = WAVLNode(key, parent=node)
                self.rebalance(node.left)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = WAVLNode(key, parent=node)
                self.rebalance(node.right)

    def inorder_debug(self):
        self._inorder_debug(self.root)
        print()

    def _inorder_debug(self, node):
        if node:
            self._inorder_debug(node.left)
            print(node.key, end=', ')
            print(node.rank, end=' | ')
            self._inorder_debug(node.right)
