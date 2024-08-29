V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

from disjointsets3 import DisjointSets

s = DisjointSets(V)

# Complete the code below
for i in edgeList:
    a,b,_ = i
    s.union(a,b)

same = True
p = s.findset(0)
for i in range(1,V):
    q = s.findset(i)
    print(f"parent of {i} is {q}, current parent is {p}")
    if p != q:
        same = False
        break

if same:
    print("connected")
else:
    print("disconnected")

    




    
