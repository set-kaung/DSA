import time

A = list(map(int,input().split()))

n = len(A)

Aux = []

st = time.process_time()

for ele in A:
    p,q = -1,0
    while q < len(Aux) and Aux[q] < ele:
        p = q
        q += 1
    Aux.insert(p+1,ele)

    
et = time.process_time()

print(Aux)
print(et-st)