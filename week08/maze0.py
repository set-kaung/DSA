# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

# The displacement for left, right, above, below
adj = [(0,-1),(0,1),(-1,0),(1,0)]

class position:
    def __init__(self, row, column):
        self.r = row
        self.c = column

def valid(r,c):  # Check whether r and c forms a walkable position
    global steps
    
    if r >= 0 and r < 10 and c >= 0 and c < 10:
        if steps[r][c] == 0:
            return True
    return False

steps = [[0]*10 for r in range(10)]  # Matrix to record steps from the start to each position
maze = []  # The maze, stored as list of string lines
ends = []  # List of positions that are marked X
visited = set()

for r in range(10):
    maze.append(input())
for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1   # -1 indicates that the position is wall
        if maze[r][c] == 'X':
            ends.append(position(r,c))

def is_destination(p):  # Test if p is the destination position
    if p.r == ends[1].r and p.c == ends[1].c:
        return True
    else:
        return False

Q = [ends[0]] 
visited.add((Q[0].r, Q[0].c))  # Enqueue the start position
while not is_destination(Q[0]):
    # Considering the position at the queue's front
    u = Q[0]
    del Q[0]  # Dequeue as Q[0] is already copied to u
    for d in adj:   # Loop through the positions adjacent to u
        nr, nc = d
        newr, newc = nr+u.r,nc+u.c
        if valid(newr,newc) and (newr,newc) not in visited:
            visited.add((newr,newc))
            steps[newr][newc] = steps[u.r][u.c] + 1
            Q.append(position(newr,newc))  
        

print(steps[Q[0].r][Q[0].c])

                


        

