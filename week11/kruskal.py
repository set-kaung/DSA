# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

from disjointsets3 import DisjointSets

V,E = map(int, input().split())
edgeList = []
for _ in range(E):
    edgeList.append(tuple(map(int, input().split())))

def getWeight(i):
    return i[2]


# initialise the disjoint sets with vertices
disjointSets = DisjointSets(V)


# sort edges by weight
edgeList.sort(key=getWeight)

total = 0

for i in range(V):
    start,end,w = edgeList[i]
    if disjointSets.findset(start) != disjointSets.findset(end):
        total += w
        disjointSets.union(start,end)

print(total)
