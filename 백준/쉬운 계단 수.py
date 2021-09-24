import sys

n = int(sys.stdin.readline().rstrip())
dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(101)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
dp[2] = [1,1,2,2,2,2,2,2,2,1]

for i in range(3, 101):
    for j in range(10):
        if j == 0:
            dp[i][j] = (dp[i-1][j+1]) % 1000000000
        elif j == 9:
            dp[i][j] = (dp[i-1][j-1]) % 1000000000
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[n]) % 1000000000)