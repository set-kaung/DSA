# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

from Heap import heap
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
path = []



for _ in range(E):
    u,v,w = map(int,input().split())
    adj_list[u-1].append((v-1,w))




def getKey(n):
    return n.val



for i in range(len(distances)):
    print(f"{i+1} {distances[i]}")












