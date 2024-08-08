# Name: Set Kaung Lwin
# ID: 6630271
# Sec. 543

# r can either be middle or last
def merge(A, p, q, r):
    i = p 
    j = q + 1 

    for k in range(p, r + 1):
        if i <= q and (j > r or A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

    # update A
    for k in range(p, r + 1):
        A[k] = B[k]
    # merge the sorted A[p:q+1] with the sorted A[q+1:r+1]
    # the result is a sorted A[p:r+1]
    # Hint: an auxiliary list is required
    # Complete the body of this function
    

def mergesort(A, p, r):
    if r - p <= 0:
        return 
    middle = (p+r)//2
    mergesort(A,p,middle)
    mergesort(A,middle+1,r)
    merge(A,p,middle,r)

a = list(map(int, input().split()))

# a = [3,1,7,5,6]

import time

st = time.process_time()

B = [0] * len(a) 

mergesort(a, 0, len(a)-1)

et = time.process_time()

# print(a)
print(et-st)
