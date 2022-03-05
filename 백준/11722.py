import sys
##방법2
# n = int(sys.stdin.readline().rstrip())
# inputs = list(map(int, sys.stdin.readline().split()))
# dp = [1] * n
#
# for i in range(n):
#     for j in range(i):
#         if inputs[i] < inputs[j]:
#             if dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#
# print(max(dp))

##방법3
n = int(sys.stdin.readline().rstrip())
inputs = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if inputs[i] > inputs[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
print(max(dp))