import random
import threading
import collections
from threading import RLock

#lock = RLock()

mylist = []
for i in range(0, 50000000):
    x = random.randint(-10, 10)
    mylist.append(x)

mid = len(mylist) // 2

L = mylist[:mid]
R = mylist[mid:]
histL = {}
histR = {}

def thread_A():
    print("trhead A start")
    #with lock:
    for l in L:
        histL[l] = histL.get(l, 0) + 1


def thread_B():
    print("Thread B start")
    #with lock:
    for r in R:
        histR[r] = histR.get(r, 0) + 1


def count_elements(seq) -> dict:
    #with lock:
        hist = {}
        for c in seq:
            hist[c] = hist.get(c, 0) + 1
        return hist


t1 = threading.Thread(target=thread_A())
t2 = threading.Thread(target=thread_B())

t1.start()
t2.start()

t1.join()
t2.join()

# a1 = count_elements(L)
# a2 = count_elements(R)

aR_counter = collections.Counter(histR)
aL_counter = collections.Counter(histL)
#
# a_counter = collections.Counter(a1)
# b_counter = collections.Counter(a2)

# out1 = a_counter + b_counter
# out1 = dict(out1)
# print("Split, no thread", out1)

out2 = aR_counter + aL_counter
out2 = dict(out2)
print("Thread", out2)

# a3 = count_elements(mylist)
# print("No split to thread, just count", a3)

# if out1 == a3 == out2:
#     print("You've done this, they are all equal!!!")

