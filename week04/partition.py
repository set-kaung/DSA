# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

import sys

sys.setrecursionlimit(10000)

counter = 0

def partition(A, p, r):  # Lomuto's partition scheme
    global counter
    x = A[r]
    i = p-1
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1

def quicksort(a,q,r):
    if q < r:
        i = partition(a,q,r)
        print(a[q:i], a[i], a[i+1:r+1])
        quicksort(a,q,i-1)
        quicksort(a,i+1,r)


# a = list(map(int,input().split()))
A = [52, 37, 63, 14, 17, 8, 6, 25]
quicksort(A,0,len(A)-1)

print(A)
print(counter)


