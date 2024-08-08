import time
a = list(map(int, input().split()))

result = ""

dic = {}

st = time.process_time()
for i in range(len(a)):
    if result != "":
        break
    for j in range(i+1, len(a)):
        x,y = a[i],a[j]
        res = x * y
        print(i,j)
        if res in dic:
            b,c = dic[res]
            if b != x and c != y and b != y and c != x:
                result += f"{b} {c}, {x} {y} "
                break
        else:
            dic[res] = (x, y)

et = time.process_time()
if result != "":
    print(result)
else:
    print("There is no such pairs")

print(et-st)
        
    
