# Soe Phone Pyae
# 6712143
# Section - 542

import time


K = int(input())
a = list(map(int, input().split()))


st = time.process_time()
found = False
ans_dict = dict()


for x in a:
    if K % x == 0:
        y = K // x
        ans_dict[y] = x


for key in ans_dict:
    if ans_dict[key] in ans_dict:
        found = True
        break


et = time.process_time()

if found:
    print(f"{ans_dict[key]} {int(key)}")
else:
    print("no match found")

print(et - st)
