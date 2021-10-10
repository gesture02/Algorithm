import sys

n = int(sys.stdin.readline().rstrip())
input = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = input[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + input[i], input[i])

print(max(dp))