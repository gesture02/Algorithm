import sys

n = int(sys.stdin.readline().rstrip())
inputs = list(map(int, sys.stdin.readline().split()))

dp = [i for i in inputs]

for i in range(1, n):
    dp[i] = max(dp[i-1]+inputs[i], inputs[i])

print(max(dp))