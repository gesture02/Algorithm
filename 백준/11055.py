import sys

n = int(sys.stdin.readline().rstrip())
input = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = input[0]

for i in range(1, n):
    dp[i] = input[i]
    for j in range(i):
        if input[i] > input[j]:
            if dp[i] < dp[j] + input[i]:
                dp[i] = dp[j] + input[i]
print(max(dp))