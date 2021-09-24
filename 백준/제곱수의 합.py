import math
import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * 100001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    minv = sys.maxsize
    for j in range(1, int(math.sqrt(i)) + 1):
        if minv > dp[i - j*j]:
            minv = dp[i - j * j]
    dp[i] = minv + 1
print(dp[n])