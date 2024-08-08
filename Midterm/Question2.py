# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

a = list(map(float,input().split()))

freq = 0 
dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    if dic[i] > freq:
        freq = dic[i]

print(freq-1)