def print_list(list):
    for i in range(len(list)):
        print(f"{i:2d}: {list[i]}")

V,E = map(int, input().split())


adj_list = [[] for _ in range(E)]

for _ in range(E):
    r,c = map(int,input().split())
    adj_list[r].append(c)

print_list(adj_list)
    