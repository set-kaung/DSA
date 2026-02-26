from pprint import pprint
row, col = map(int,input().split())
sr,sc = map(int,input().split())
dr,dc = map(int,input().split())

maze = [[] for _ in range(row)]
for i in range(row):
    maze[i] = list(map(int,input().split()))

class state:
    def __init__(self,row,col,step=0) -> None:
        self.row = row
        self.col = col
        self.step = step

def isValid(mr,mc):
    if mr >= 0 and mr < row and mc >= 0 and mc < col:
        if maze[mr][mc] == 0:
            return True
    return False

moves = [(0,1),(0,-1), (1,0), (-1,0)]

def successor(s):
    succ = []
    for move in moves:
        r = s.row + move[0]
        c = s.col + move[1]
        if isValid(r,c):
            succ.append(state(r,c,s.step+1))

    return succ

def Goal(s):
    if s.row == dr and s.col == dc:
        return True
    return False

parents = [([None]*col) for _ in range(row)]
queue = []
s = state(sr,sc)
visited = set()
visited.add((sr,sc))
while not Goal(s):
    for u in successor(s):
        if (u.row,u.col) not in visited:
            queue.append(u)
            visited.add((u.row,u.col))
            parents[u.row][u.col] = (s.row,s.col) 
    s = queue.pop(0)

maze[sr][sc] = 3
while parents[s.row][s.col]:
    x,y = parents[s.row][s.col]
    maze[s.row][s.col] = 3
    s = state(x,y)

for i in maze:
    for j in i:
        if j == 3:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
