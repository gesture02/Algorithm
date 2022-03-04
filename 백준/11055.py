import sys

n = int(sys.stdin.readline().rstrip())
inputs = list(map(int, sys.stdin.readline().split()))
dp = [i for i in inputs]

for i in range(n):
    for j in range(i):
        if inputs[i] > inputs[j]:
            if dp[i] < dp[j] + inputs[i]:
                dp[i] = dp[j] + inputs[i]

print(max(dp))