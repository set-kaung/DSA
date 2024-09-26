# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

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

distances = [node(sys.maxsize) for i in range(V)]

distances[0].key = 0
path = []

for _ in range(E):
    u,v,w = map(int,input().split())
    adj_list[u-1].append((v-1,w))



pq = heap(distances)
prev = None
while pq.heapsize > 0:
    m = pq.extract()
    u = distances[m]
    path.append(m+1)
    for (v,w) in adj_list[m]:
        if u.key+w < distances[v].key:
            pq.elevate_key(v,u.key+w)
            distances[v].prev = m+1
    prev = m
def getKey(n):
    return n.val



for i in range(len(distances)):
    print(f"{i+1} {distances[i]}")












