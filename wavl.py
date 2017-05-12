import bst

class WAVLNode(bst.Node):
    def __init__(self, key, left=None, right=None, rank=0, parent=None):
        super(WAVLNode, self).__init__(key, left, right, parent)
        self.rank = rank
        self.parent = parent

class WAVL(bst.BST):
    def __init__(self):
        super(WAVL, self).__init__()

    # adapted from CLRS edition 3, page 313
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # adapted from CLRS edition 3, page 313
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

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

    def insert_rebalance(self, node):
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
                    if y == None or curr_node.rank - y.rank == 2:
                        self.right_rotate(curr_node.parent)
                        self.demote(z)
                    else:
                        assert curr_node.rank - y.rank == 1
                        self.left_rotate(y.parent)
                        self.right_rotate(y.parent)
                        self.promote(y)
                        self.demote(curr_node)
                        self.demote(z)
                else:
                    assert curr_node == curr_node.parent.right
                    z = curr_node.parent
                    y = curr_node.left
                    if y == None or curr_node.rank - y.rank == 2:
                        self.left_rotate(curr_node.parent)
                        self.demote(z)
                    else:
                        assert curr_node.rank - y.rank == 1
                        self.right_rotate(y.parent)
                        self.left_rotate(y.parent)
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
                self.insert_rebalance(node.left)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = WAVLNode(key, parent=node)
                self.insert_rebalance(node.right)

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

    # adapted from CLRS edition 3, page 298
    def _remove(self, z):
        produces_22leaf = False
        n = None
        m = None
        par = z.parent
        produces_3child = False
        print("parent's children: ", end='')
        print(par.left, end=' ')
        print(par.right)
        print("z's rank: ", end='')
        print(z.rank)
        print("parent's rank: ", end='')
        print(par.rank)
        print("z's children: ", end='')
        print(z.left, end=' ')
        print(z.right)


        # determine how to rebalance
        if z.left == None and z.right == None and z.parent:
            m = z.parent
            if (z.parent.left == z and z.parent.right == None and z.parent.rank - z.rank == 1) or (z.parent.right == z and z.parent.left == None and z.parent.rank - z.rank == 1):
                produces_22leaf = True
        if z.parent and z.parent.rank - z.rank == 2:
            produces_3child = True

        if z.left == None:
            self.transplant(z, z.right)
            n = z.right
        elif z.right == None:
            self.transplant(z, z.left)
            n = z.left
        else:
            y = self.get_min(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            n = y

        if produces_22leaf:
            assert m == par
            assert self.rank_diffs(m) == (2, 2)
            print("here")
            self.demote(m)
            if m.parent and m.parent.rank - m.rank == 3:
                self.deletion_rebalance(m, par)
        elif produces_3child:
            if n == None:
                assert par.rank + 1 == 3
            else:
                assert par.rank - n.rank == 3
            assert par.left == n or par.right == n
            self.deletion_rebalance(n, par)

    def deletion_rebalance(self, node, parent):
        print("rebalancing")
        x = node
        y = None
        par = parent
        if x:
            assert par.rank - x.rank == 3
        else:
            assert par.rank + 1 == 3

        if x == par.left:
            y = par.right
        else:
            y = par.left

        x_rank = 0;
        if x == None:
            x_rank = -1
        else:
            x_rank = x.rank

        print("par rank: ", end='')
        print(par.rank)
        print("x rank: ", end='')
        print(x_rank)
        print("y rank: ", end='')
        print(y.rank)
        print("y rank diffs: ", end='')
        print(self.rank_diffs(y))

        while par.rank - x_rank == 3 and (par.rank - y.rank == 2 or self.rank_diffs(y) == (2, 2)):
            self.demote(par)
            if par.rank - y.rank != 2:
                self.demote(y)
            x = par
            par = par.parent
            if x == par.left:
                y = par.right
            else:
                y = par.left

            if x == None:
                x_rank = -1
            else:
                x_rank = x.rank

        rd = self.rank_diffs(par)
        if rd == (1, 3) or rd == (3, 1):
            assert self.rank_diffs(y) != (2, 2)

            if x == par.left:
                z = par
                v = y.left
                w = y.right

                if w.parent.rank - w.rank == 1:
                    self.left_rotate(y.parent) #just y?
                    self.promote(y)
                    self.demote(z)
                    if z.left == None and z.right == None:
                        self.demote(z)
                else:
                    assert w.parent.rank - w.rank == 2
                    self.right_rotate(v.parent)
                    self.left_rotate(v.parent)
                    self.promote(v)
                    self.promote(v)
                    self.demote(y)
                    self.demote(z)
                    self.demote(z)
            else:
                assert x == par.right
                z = par
                v = y.right
                w = y.left

                if w.parent.rank - w.rank == 1:
                    self.right_rotate(y.parent) #just y?
                    self.promote(y)
                    self.demote(z)
                    if z.left == None and z.right == None:
                        self.demote(z)
                else:
                    assert w.parent.rank - w.rank == 2
                    self.left_rotate(v.parent)
                    self.right_rotate(v.parent)
                    self.promote(v)
                    self.promote(v)
                    self.demote(y)
                    self.demote(z)
                    self.demote(z)

    def inorder_debug(self):
        self._inorder_debug(self.root)
        print()

    def _inorder_debug(self, node):
        if node:
            self._inorder_debug(node.left)
            print('(', end='')
            print(node.key, end=', ')
            print(node.rank, end=')')
            self._inorder_debug(node.right)

    def validate(self):
        if self.root == None:
            return True
        else:
            return self._validate(self.root)

    def _validate(self, node):
        if node.left == None and node.right == None:
            return node.rank == 0
        elif node.left and node.right:
            print(node.rank)
            print(node.left.rank)
            assert (node.rank - node.left.rank == 1 or node.rank - node.left.rank == 2)
            assert (node.rank - node.right.rank == 1 or node.rank - node.right.rank == 2)
            return (node.rank - node.left.rank == 1 or node.rank - node.left.rank == 2) and (node.rank - node.right.rank == 1 or node.rank - node.right.rank == 2) and self._validate(node.left) and self._validate(node.right)
        elif node.left:
            assert (node.rank - node.left.rank == 1 or node.rank - node.left.rank == 2)
            return (node.rank - node.left.rank == 1 or node.rank - node.left.rank == 2) and self._validate(node.left)
        else:
            assert (node.rank - node.right.rank == 1 or node.rank - node.right.rank == 2)
            return (node.rank - node.right.rank == 1 or node.rank - node.right.rank == 2) and self._validate(node.right)
