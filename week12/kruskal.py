# import pprint
V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

def weight(i):
    return i[2]


from disjointsets3 import DisjointSets

s = DisjointSets(V)
edgeList.sort(key=weight)
total = 0
for e in edgeList:
    st,des,w = e
    if s.findset(st) != s.findset(des):
        total += w
        s.union(st,des)


print(total)