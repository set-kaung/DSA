from disjointsets3 import DisjointSets
import time
 
 
def get_neighbors(x, y, image):
    neighbors = []
    if ((x-1) in range(M)) and image[x-1][y] == 1:
        neighbors.append(((x-1)*N)+y)
    if ((x+1) in range(M)) and image[x+1][y] == 1:
        neighbors.append(((x+1)*N)+y)
    if ((y-1) in range(N)) and image[x][y-1] == 1:
        neighbors.append((x*N)+(y-1))
    if ((y+1) in range(N)) and image[x][y+1] == 1:
        neighbors.append((x*N)+(y+1))
 
    return neighbors
 
 
st = time.process_time()
M, N = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(M)]
S = DisjointSets(M*N)
clouds = []
 
for x in range(len(image)):
    for y in range(len(image[x])):
        if image[x][y] == 1:
            coordinate = (x*N)+y
            clouds.append(coordinate)
            neighbors = get_neighbors(x, y, image)
            for n in neighbors:
                S.union(coordinate, n)
 
et = time.process_time()
print(et - st)
sizes = {}
largest = 0


for current_row in range(M):
    for current_column in range(N):
        if image[current_row][current_column] == 1:
            representative = S.findset(current_row*N+current_column)
            if representative in sizes:
                sizes[representative] += 1
            else:
                sizes[representative] = 1
            largest = max(sizes[representative],largest)

print(largest)