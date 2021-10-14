import sys

n = int(sys.stdin.readline().rstrip())
input = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if input[i] > input[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
idx = max(dp)
result = []
print(idx)
for i in range(n-1, -1, -1):
    if dp[i] == idx:
        result.append(input[i])
        idx -= 1
print(*result[::-1])