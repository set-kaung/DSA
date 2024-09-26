import random

row,col = 30,20

print(f"{row} {col}")


for i in range(row):
    for j in range(col):
        print(random.randrange(0,3)%2,end=" ")
    print()
