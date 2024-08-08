graph = {"A": ["B", "C"], "B": ["D", "F"], "C": ["D"], "D": ["F"], "F":["E"]}
source = "A"
target = "E"
visited = []
candid = []
candid.append(source)
lc = len(candid)
parent = {}
path = []
parent[source] = None
while lc != 0:
    p = candid[0]
    candid = candid[1:]
    visited.append(p)
    
    if p == target:
        path = [p]
        while parent[p] in parent:
            p = parent[p]
            path.append(p)
        path.reverse()
        if path[0] != source:
            path = []
        break
        
    for i in graph[p]:
        if i not in visited:
            visited.append(i)
            candid.append(i)
            parent[i] = p

    lc = len(candid)
    
print(path)
