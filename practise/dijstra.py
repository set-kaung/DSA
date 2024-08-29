from collections import deque
from pprint import pprint
V,E = map(int,input().split())


routers = {'u':0, 'v':1,'w':2, 'x':3,'y':4,'z':5}
adj = [[0.0]*V for _ in range(V)]
for _ in range(E):
    s,d,w = input().split()
    s = routers[s]
    d = routers[d]
    w = float(w)
    adj[s][d], adj[d][s] = w,w

distances = [[float('inf')]*V for _ in range(V)]

start = routers['u']
end = routers['z']

# visited = set()




pprint(adj)


