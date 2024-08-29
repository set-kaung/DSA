# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543
def print_list(lst):
    for i in range(len(lst)):
        print(f"{i:2d}: {lst[i]}")

V,E = map(int, input().split())


adj_list = [[] for _ in range(V)]

for _ in range(E):
    r,c = map(int,input().split())
    adj_list[r].append(c)

print_list(adj_list)


from topological_sort import *

res = topological_sort(V,adj_list)
print(res)

