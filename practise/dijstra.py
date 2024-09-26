
from pprint import pprint
import sys
V,E = map(int,input().split())


routers = {'u':0, 'v':1,'w':2, 'x':3,'y':4,'z':5}
adj_list = [[] for _ in range(V)]
for _ in range(E):
    s,d,w = input().split()
    s = routers[s]
    d = routers[d]
    w = float(w)
    adj_list[s].append((d,w))

distances = [sys.maxsize]*V


start = routers['u']
end = routers['z']
visited = set()

for d,w in adj_list[s]:
    distances[d] = w

next = start
path = str(start)
while next != end:
    x = adj_list[next][:]
    x.sort(key=lambda y: y[1])
    shortest = x[0]
    path = path + str(shortest[0])
    for k,w in adj_list[shortest[0]]:
        distances[k] = min(distances[k],distances[shortest[0]] + w)
    next = shortest[0]

path = list(path)
for i in range(len(path)):
    for k,v in routers.items():
        if path[i] == str(v):
            path[i] = k

print(path)
        
    









