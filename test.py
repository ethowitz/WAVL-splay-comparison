import bst
import wavl
import splay

print("<<<<<<<<<<<<<<<<<<<< BST TESTS >>>>>>>>>>>>>>>>>>>>>>>")
b = bst.BST()
b.insert(5)
b.inorder()
b.insert(1)
b.inorder()
b.insert(7)
b.inorder()
b.insert(2)
b.inorder()
b.insert(6)
b.inorder()
# b.insert(12)
# b.insert(4)
# b.insert(0)
# b.insert(11)
# b.insert(13)
# b.insert(14)
# b.insert(15)
# b.insert(16)
# b.insert(17)
# b.insert(18)
# b.insert(19)
# b.inorder()
# b.remove(5)
# b.remove(12)
# b.remove(4)
# b.inorder()
# assert not b.search(5)
# assert not b.search(12)
# assert not b.search(4)
# print('height: ', end='')
# print(b.height())

print("<<<<<<<<<<<<<<<<<<<< WAVL TESTS >>>>>>>>>>>>>>>>>>>>>>>")
w = wavl.WAVL()
w.insert(5)
w.insert(1)
w.insert(7)
w.insert(8)
w.insert(6)
w.insert(2)
w.insert(6)
w.insert(12)
w.insert(4)
w.insert(0)
w.insert(11)
w.insert(13)
w.insert(14)
w.insert(15)
w.insert(16)
w.insert(17)
w.insert(18)
w.insert(19)
w.inorder()
w.remove(5)
assert w.validate()
w.remove(7)
assert w.validate()
assert not w.search(7)
w.remove(4)
assert w.validate()
assert not w.search(4)
w.remove(14)
assert w.validate()
assert not w.search(14)
w.remove(16)
assert w.validate()
assert not w.search(16)
w.inorder()

# print('height: ', end='')
# print(w.height())

print("<<<<<<<<<<<<<<<<<<<< SPLAY TESTS >>>>>>>>>>>>>>>>>>>>>>>")
s = splay.Splay()
s.insert(5)
s.insert(1)
s.insert(7)
s.insert(8)
s.insert(6)
s.insert(2)

s.remove(8)
s.print_root()
s.remove(1)
s.print_root()
s.remove(5)
s.print_root()
s.remove(7)
s.print_root()
