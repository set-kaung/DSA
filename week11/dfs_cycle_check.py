def findRedundantConnection(edges:list[list[int]]) -> list[int]:
    result = []
    adjList = {}
    for i in edges:
        u,v = i[0],i[1]
        if u in adjList:
            adjList[u].append(v)
        else:
            adjList[u] = [v]
        if v in adjList:
            adjList[v].append(u)
        else:
            adjList[v] = [u]

    def dfs(parent,current,visited):
        visited.add(current)
        for child in adjList[current]:
            if child not in visited:
                if dfs(current,child,visited):
                    return True
            if child != parent:
                return True
        return False
    
    result = []
    visited = set()
    for i in  edges:
        u,v = i[0],i[1]
        if dfs(u,v,visited):
            result.append([u,v])
    return result[-1]

print(findRedundantConnection([[1,3],[3,4],[1,5],[3,5],[2,3]]))