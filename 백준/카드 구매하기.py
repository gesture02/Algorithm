import sys

n = int(sys.stdin.readline().rstrip())
input = [0]
input += list(map(int, sys.stdin.readline().split()))
dp = [0] * 1001
dp[1] = input[1]

for i in range(2, n+1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[i-j] + input[j])

print(dp[n])