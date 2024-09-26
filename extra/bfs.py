from pprint import pprint
n = int(input())

adjList = [[] for _ in range(n)]

for _ in range(n):
    x = list(map(int,input().split()))
    u = x[0]
    for v in x[2:]:
        adjList[u-1].append(v-1)
        
distances = [-1]*n
distances[0] = 0

q = [0]

while len(q) != 0:
    s = q.pop(0)
    for e in adjList[s]:
        if distances[e] == -1:
            distances[e] = distances[s]+1
            q.append(e)

for i in range(len(distances)):
    print(i+1,distances[i])