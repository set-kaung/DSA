graph_type = input()
V,E = map(int, input().split())
adj_list = [[] for v in range(V)]

def print_list(ls):
    for i in ls:
        for j in i:
            print(j+1, end=" ")
        print()

for i in range(E):
    u,v = map(int, input().split())
    u -= 1 # parent - 1
    v -= 1 # child - 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

print_list(adj_list)
GRAY = "GRAY"

color = ["WHITE"]*V
d = [-1]*V
p = [None]*V

# Write your Breadth-First Search code below

queue = [0]
d[0] = 0

while len(queue) != 0:
    s = queue.pop(0)
    for u in adj_list[s]:
        if color[u] == "WHITE":
            color[u] = GRAY
            d[u] = d[s] + 1
            p[u] = s
            queue.append(u)

    color[s] = "BLACK"

    

# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print("%d %5s" % (v+1, color[v]), dv, pv)

