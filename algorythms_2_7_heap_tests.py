from algorythms_2_7_heap import *
import random

a = []
while len(a) < 11:
    x = random.randint(1,11)
    if x not in a:
        a.append(x)

print(a)

heap = Heap()
heap.MakeHeap(a, 1)

print(heap)

print(heap.GetMax())
print(heap)
