# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

rows,columns = map(int,input().split())

image = [[] for _ in range(rows)]

for current_row in range(len(image)):
    image[current_row] = list(map(int,input().split()))

from disjointsets3 import DisjointSets
def printImage(m):
    for i in m:
        print(i)

moves =[(-1,0),(1,0),(0,1),(0,-1)] # up down right left

def isValid(tr,tc):
    return tr >= 0 and tr < rows and tc >=0 and tc < columns

def sides(r,c):
    valid_moves = []
    for (i,j) in moves:
        tr = r+i
        tc = c+j
        if isValid(tr,tc):
            valid_moves.append((tr,tc))

    return valid_moves




ds = DisjointSets(rows*columns)


largest = 0

for current_row in range(len(image)):
    for current_column in range(len(image[current_row])):
        if image[current_row][current_column] == 1:
            for (neighbor_row,neighbor_col) in sides(current_row,current_column):
                if image[neighbor_row][neighbor_col] == 1:
                    ds.union( ( neighbor_row*columns+neighbor_col ) , ( current_row*columns+current_column ) )

sizes = {}    
        
for current_row in range(rows):
    for current_column in range(columns):
        if image[current_row][current_column] == 1:
            representative = ds.findset(current_row*columns+current_column)
            if representative in sizes:
                sizes[representative] += 1
            else:
                sizes[representative] = 1
            largest = max(sizes[representative],largest)

print(largest)
                





    
