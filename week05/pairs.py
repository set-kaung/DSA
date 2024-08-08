# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

N = int(input())
A = list(map(int,input().split()))
dic1 = {}
for i in range(len(A)):
    dic1[((i+1)**2)+A[i]] = dic1.get(((i+1)**2)+A[i],0) + 1
 
count = 0
for j in range(len(A)-1,-1,-1):
    if A[j]-((j+1)**2) in dic1:
        count += dic1[A[j]-((j+1)**2)]
        
print(count)