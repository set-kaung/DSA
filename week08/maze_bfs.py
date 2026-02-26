from collections import deque
import math
adj = [(0,-1),(0,1),(-1,0),(1,0)]

class position:
    def __init__(self, row, column):
        self.r = row
        self.c = column
        self.step = 0


 # Matrix to record steps from the start to each position
maze = []  # The maze, stored as list of string lines
ends = []  # List of positions that are marked X
visited = set()

for r in range(10):
    maze.append(input())
    
for r in range(10):
    for c in range(10):  # -1 indicates that the position is wall
        if maze[r][c] == 'X':
            ends.append(position(r,c))


def heuristic(new,prev):
    nx = abs(ends[1].r-new.r)
    ny = abs(ends[1].c-new.c)
    px = abs(ends[1].r-prev.r)
    py = abs(ends[1].c-prev.c)
    odist = math.sqrt(px**2 + py**2)
    ndist = math.sqrt(nx**2 + ny**2)
    return ndist - odist < 3



def isGoal(p):
    if ends[1].r == p.r and ends[1].c == p.c:
        return True
    return False

def isValid(p):
    if p.r >=0 and p.c >= 0 and p.r < len(maze) and p.c < len(maze[0]):
        return maze[p.r][p.c] != "#"

def successors(p):
    succ = []
    for move in adj:
        newPosition = position(p.r+move[0],p.c+move[1])
        if isValid(newPosition):
            newPosition.step = p.step + 1
            succ.append(newPosition)
    return succ


stack = deque()
stack.append(ends[0])
current = stack.popleft()

while not isGoal(current):
    visited.add((current.r,current.c))
    for s in successors(current):
        if (s.r,s.c) not in visited:
            stack.append(s)
    current = stack.popleft()

print(current.step)