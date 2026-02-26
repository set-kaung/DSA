# # Name: Set Kaung Lwin
# # ID: 6632017
# # Sec: 543

from Heap_Decrease_Key import heap
import sys

class node:
    def __init__(self,key,prev=None) -> None:
        self.prev = prev
        self.key = key

    def __str__(self) -> str:
        return f"{self.key} {self.prev}"

input()
V,E = map(int,input().split())
adj_list = [[] for _ in range(V)]

distances:list[node] = [node(sys.maxsize) for _ in range(V)]

distances[0].key = 0

for _ in range(E):
   u,v,w = map(int,input().split())
   adj_list[u-1].append((v-1,w))

pq = heap(distances)
while pq.heapsize > 0:

    # get index of min item
    m = pq.extract()

    # get min item
    u = distances[m]
    
    for (v,w) in adj_list[m]:
        if u.key+w < distances[v].key:
            pq.elevate_key(v,u.key+w)
            distances[v].prev = m+1

def getKey(n):
    return n.val

print(adj_list)

for i in range(len(distances)):
    print(f"{i+1} {distances[i]}")

