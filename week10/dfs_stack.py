from collections import deque

graph_type = input()
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]
for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)

color = ["WHITE"] * V
p = [None] * V
time = 0
d = [-1] * V
f = [-1] * V

stack = deque()
stack.append(0)
def dfs_visit(start_node):
    global time
    stack = deque()
    stack.append(start_node)
    while stack:
        current = stack.pop()
        if color[current] == "WHITE":
            # First time visiting this node
            time += 1
            d[current] = time
            color[current] = "GRAY"
            # Add current node back to the stack to assign finishing time later
            stack.append(current)
            # Add all unvisited neighbors to the stack
            for neighbor in adj_list[current][::-1]:
                if color[neighbor] == "WHITE":
                    p[neighbor] = current
                    stack.append(neighbor)
        elif color[current] == "GRAY":
            # All neighbors have been processed, so finish this node
            time += 1
            f[current] = time
            color[current] = "BLACK"

for v in range(V):
    if color[v] == "WHITE":
        dfs_visit(v)

# Output the discovery, finishing times, and parent information
for v in range(V):
    if d[v] == -1:
        dv = "undiscovered"
    else:
        dv = d[v]
    if f[v] == -1:
        fv = ""
    else:
        fv = f[v]
    if p[v] is not None:
        pv = p[v] + 1  # Convert back to 1-indexed
    else:
        pv = "None"

    print(f"{v+1} {color[v]:>5} {dv} {fv} {pv}")

