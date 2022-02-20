import sys

n, m = map(int, sys.stdin.readline().split())
dp = [[0] * (n+1) for _ in range(m+1)]

dp[0][0] = 1

for k in range(1, m+1):
    for i in range(n+1):
        for j in range(i+1):
            dp[k][i] += (dp[k-1][i-j]) % 1000000000

print(dp[m][n] % 1000000000)