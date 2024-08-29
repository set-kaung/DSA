# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543
from topological_sort import *
def print_list(lst):
    for i in range(len(lst)):
        print(f"{i:2d}: {lst[i]}")

V,E = map(int, input().split())


adj_list = [[] for _ in range(V)]

for _ in range(E):
    r,c = map(int,input().split())
    adj_list[r].append(c)

res = topological_sort(V,adj_list)
print(res)