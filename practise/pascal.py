from pprint import pprint
row = int(input())
row = row+1

dp = [[0]*row for _ in range(row)]

dp[0][0] = 1

for i in range(1,row):
    for j in range(1,row):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

pprint(dp)



