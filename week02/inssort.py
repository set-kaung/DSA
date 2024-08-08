# Name: Set Kaung Lwin
# ID: 6630271
# Sec. 543

import time

a = list(map(int, input().split()))
# a = [3,7,1,4,-1,0,2]
n = len(a)

st = time.process_time()

i = 0

## n
while i < n-1:
    j = i + 1
    # first element? and sorted?
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1
    i += 1


    
et = time.process_time()

# print(a)
print(et-st)
