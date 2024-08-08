import sys

n = int(sys.argv[1])

# quicksort test case gen

import random

k = 0
while k < n:
    i = random.randint(0, 4*n)-2*n
    p = random.randint(0,10000)/10000
    if p <= 0.25:
        print(i, end=' ')
        k += 1

