V,E = map(int, input().split())
edgeList = []
adj_list = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

from Heap import heap


def cmpM(i,j):
    return i[2] < j[2]

def Prim(V,adj_list) -> int:
    total_weight = 0
    visited = set()

    visited.add(0)
    h = heap(cmp=cmpM)

    for v,w in adj_list[0]:
        h.insert((0,v,w))

    while len(visited) < V and not h.empty():
        u,v,w = h.extract()
        if v not in visited:
            total_weight += w
            visited.add(v)

            for to,weight in adj_list[v]:
                if to not in visited:
                    h.insert((v,to,weight))
    
    return total_weight




print(Prim(V,adj_list=adj_list))







