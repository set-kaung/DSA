# Name: Set Kaung Lwin
# ID: 6632017
# Sec.: 543


K = int(input())
a = list(map(int, input().split()))




import time

st = time.process_time()



memo = set(a)

found = False

for x in a:
    if x == 0:
        continue
    y = K/x
    if y in memo:
        if y != x:
            found = True  
            
    if found:
        break

et = time.process_time()

if not found:
    print("no pair exists")
else:
    print(x, int(y))


print(f"Set-based running time: {et - st}")