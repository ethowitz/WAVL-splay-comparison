import bst
import wavl
import splay
import random

MAX = 10000

def gen_accesses(n):
    accesses = []
    for i in range(n):
        accesses.append(random.randint(0, MAX))
    return accesses

def insertions(data, tree):
    for datum in data:
        tree.insert(datum)

def accesses(accs, tree):
    for a in accs:
        tree.search(a)

def deletions(ds, tree):
    for d in ds:
        tree.remove(d)

# TODO: add while loop, collect averages

data = random.sample(range(MAX), 8000)
dels = random.sample(data, 1000)
even_accesses = gen_accesses(1000)
uneven_accesses = [int(random.expovariate(0.001)) for i in range(1000)]

b = bst.BST()
w = wavl.WAVL()
s = splay.Splay()

# TODO: judge based on height, results are as expected
insertions(data, b)
deletions(dels, b)
insertions(data, w)
deletions(dels, w)
insertions(data, s)
deletions(dels, s)
print(b.height())
print(w.height())
print(s.height())

# TODO: gen new data, add to new trees, time these
accesses(uneven_accesses, s)
accesses(uneven_accesses, w)
accesses(uneven_accesses, b)
