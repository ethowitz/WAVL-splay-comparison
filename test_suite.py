import bst
import wavl
import splay
import random
import time

MAX = 10000
NUM_ROUNDS = 10

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

avg_uni_b = 0
avg_pretty_uneven_b4 = 0
avg_pretty_uneven_b10 = 0
avg_very_uneven_b = 0
avg_inter_b = 0
avg_del_b = 0

avg_uni_w = 0
avg_pretty_uneven_w4 = 0
avg_pretty_uneven_w10 = 0
avg_very_uneven_w = 0
avg_inter_w = 0
avg_del_w = 0

avg_uni_s = 0
avg_pretty_uneven_s4 = 0
avg_pretty_uneven_s10 = 0
avg_very_uneven_s = 0
avg_inter_s = 0
avg_del_s = 0

for i in range(NUM_ROUNDS):
    data = random.sample(range(MAX), MAX)
    dels = random.sample(data, 1000)
    even_accesses = random.sample(data, MAX)
    very_uneven_accesses = []
    element = data[random.randint(0, MAX)]
    for i in range(MAX):
        very_uneven_accesses.append(element)

    pretty_uneven_accesses4 = []
    base = random.randint(0, MAX - 4)
    for i in range(MAX):
        pretty_uneven_accesses4.append(random.randint(base, base + 4))

    pretty_uneven_accesses10 = []
    base = random.randint(0, MAX - 10)
    for i in range(MAX):
        pretty_uneven_accesses10.append(random.randint(base, base + 10))

    b = bst.BST()
    w = wavl.WAVL()
    s = splay.Splay()
    insertions(data, b)
    insertions(data, w)
    insertions(data, s)

    # uniform accesses
    start = time.process_time()
    accesses(even_accesses, b)
    end = time.process_time()
    avg_uni_b += end - start

    start = time.process_time()
    accesses(even_accesses, w)
    end = time.process_time()
    avg_uni_w += end - start

    start = time.process_time()
    accesses(even_accesses, s)
    end = time.process_time()
    avg_uni_s += end - start

    # nonuniform accesses
    start = time.process_time()
    accesses(pretty_uneven_accesses4, b)
    end = time.process_time()
    avg_pretty_uneven_b4 += end - start

    start = time.process_time()
    accesses(pretty_uneven_accesses4, w)
    end = time.process_time()
    avg_pretty_uneven_w4 += end - start

    start = time.process_time()
    accesses(pretty_uneven_accesses4, s)
    end = time.process_time()
    avg_pretty_uneven_s4 += end - start

    start = time.process_time()
    accesses(pretty_uneven_accesses10, b)
    end = time.process_time()
    avg_pretty_uneven_b10 += end - start

    start = time.process_time()
    accesses(pretty_uneven_accesses10, w)
    end = time.process_time()
    avg_pretty_uneven_w10 += end - start

    start = time.process_time()
    accesses(pretty_uneven_accesses10, s)
    end = time.process_time()
    avg_pretty_uneven_s10 += end - start

    start = time.process_time()
    accesses(very_uneven_accesses, b)
    end = time.process_time()
    avg_very_uneven_b += end - start

    start = time.process_time()
    accesses(very_uneven_accesses, w)
    end = time.process_time()
    avg_very_uneven_w += end - start

    start = time.process_time()
    accesses(very_uneven_accesses, s)
    end = time.process_time()
    avg_very_uneven_s += end - start

    # test cases for deletion
    start = time.process_time()
    deletions(dels, b)
    end = time.process_time()
    avg_del_b += end - start

    start = time.process_time()
    deletions(dels, w)
    end = time.process_time()
    avg_del_w += end - start

    start = time.process_time()
    deletions(dels, s)
    end = time.process_time()
    avg_del_s += end - start

print("<<<<<<<< Uniform Access Results (in seconds) >>>>>>>>")
print("BST: ", avg_uni_b / NUM_ROUNDS)
print("WAVL: ", avg_uni_w / NUM_ROUNDS)
print("Splay: ", avg_uni_s / NUM_ROUNDS)

print("<<<<<<<< Single Element Queried Repeatedly Results (in seconds) >>>>>>>>")
print("BST: ", avg_very_uneven_b / NUM_ROUNDS)
print("WAVL: ", avg_very_uneven_w / NUM_ROUNDS)
print("Splay: ", avg_very_uneven_s / NUM_ROUNDS)

print("<<<<<<<< Same 4 Elements Queried Randomly (in seconds) >>>>>>>>")
print("BST: ", avg_pretty_uneven_b4 / NUM_ROUNDS)
print("WAVL: ", avg_pretty_uneven_w4 / NUM_ROUNDS)
print("Splay: ", avg_pretty_uneven_s4 / NUM_ROUNDS)

print("<<<<<<<< Same 10 Elements Queried Randomly (in seconds) >>>>>>>>")
print("BST: ", avg_pretty_uneven_b10 / NUM_ROUNDS)
print("WAVL: ", avg_pretty_uneven_w10 / NUM_ROUNDS)
print("Splay: ", avg_pretty_uneven_s10 / NUM_ROUNDS)

print("<<<<<<<< Deleting 1000 Elements (in seconds) >>>>>>>>")
print("BST: ", avg_del_b / NUM_ROUNDS)
print("WAVL: ", avg_del_w / NUM_ROUNDS)
print("Splay: ", avg_del_s / NUM_ROUNDS)
