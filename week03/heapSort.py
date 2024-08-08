import time
from Heap import heap


A = list(map(int, input().split()))


n = len(A)

def checkoutMax(h):
    return h.extract()

def maxcompare(x,y):
    return x > y



st = time.process_time()  

h = heap(items=A,cmp=maxcompare) 

for i in range(n-1, -1, -1):
    checkoutMax(h)

et = time.process_time()

print(A)
print(et-st)