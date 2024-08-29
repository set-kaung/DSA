# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543
def print_matrix(matrix):
    rows = len(matrix)
    print("    ",end="") 
    for i in range(rows):
        print(f"{i}", end=" ")
    print(end="\n\n")

    for i in range(len(matrix)):
        print(f"{i:2d}  ", end="")
        for j in matrix[i]:
            print(f"{j}", end=" ") 
        print()
        


V,E = map(int, input().split())

adjMatrix = [[0]*(V) for _ in range(V)]

for _ in range(E):
    r,c = map(int,input().split())
    adjMatrix[r][c] = 1


print_matrix(adjMatrix)