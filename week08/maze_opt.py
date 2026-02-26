from collections import deque
import heapq

adj = [(0,1),(0,-1), (1,0), (-1,0)]

class Position:
    def __init__(self, row, column, step=0, cost=0):
        self.r = row
        self.c = column
        self.step = step
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

# Matrix to record steps from the start to each position
row, col = map(int, input().split())
sr, sc = map(int, input().split())
dr, dc = map(int, input().split())

maze = [[] for _ in range(row)]
for i in range(row):
    maze[i] = input().split()

def heuristic(p):
    # Use Manhattan distance for a simpler and faster heuristic
    return abs(dr - p.r) + abs(dc - p.c)

def isGoal(p):
    return dr == p.r and dc == p.c

def isValid(p):
    return 0 <= p.r < len(maze) and 0 <= p.c < len(maze[0]) and maze[p.r][p.c] != "1"

def successors(p):
    succ = []
    for move in adj:
        newPosition = Position(p.r + move[0], p.c + move[1], p.step + 1)
        if isValid(newPosition):
            newPosition.cost = newPosition.step + heuristic(newPosition)
            succ.append(newPosition)
    return succ

priority_queue = []
heapq.heappush(priority_queue, Position(sr, sc, 0, heuristic(Position(sr, sc))))

visited = set()
count = 0

while priority_queue:
    current = heapq.heappop(priority_queue)
    if isGoal(current):
        print(current.step)
        print(f"tried {count} places")
        break

    visited.add((current.r, current.c))
    count += 1

    for s in successors(current):
        if (s.r, s.c) not in visited:
            heapq.heappush(priority_queue, s)
else:
    print("No path found")
    print(f"tried {count} places")