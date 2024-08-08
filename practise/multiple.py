A = list(map(int,input().split()))

dic = {}

result = []

i = 0
found = False

while i < len(A) and not found:
    j = i+1
    while j < len(A) and not found:
        multi = A[i]*A[j]
        if multi in dic and A[i]: #not in dic[multi] and A[j] not in dic[multi]:
            result = dic[multi]
            result.append(A[i])
            result.append(A[j])
            found = True
            break
        else:
            dic[multi] = [A[i],A[j]]
        j+=1
    i+=1

if len(result) != 0:
    print(f"{result[0]} {result[1]} , {result[2]} {result[3]} ")
else:
    print("No pair exists")


            
