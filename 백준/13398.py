import sys

n = int(sys.stdin.readline().rstrip())
inputs = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp2 = [0] * n
dp[0] = inputs[0]
dp2[n-1] = inputs[n-1]

for i in range(1, n):
    dp[i] = max(dp[i-1] + inputs[i], inputs[i])

for i in range(n-2, -1, -1):
    dp2[i] = max(dp2[i+1] + inputs[i], inputs[i])

answer = max(dp)
for i in range(1, n-1):
    if answer < dp[i-1] + dp2[i+1]:
        answer = dp[i-1] + dp2[i+1]

print(answer)


# n = int(sys.stdin.readline().rstrip())
# input = list(map(int, sys.stdin.readline().split()))
# dp = [[0] * n for _ in range(2)]
# dp[0][0] = input[0]
# dp[1][0] = input[0]
#
# for i in range(1, n):
#     dp[0][i] = max(dp[0][i-1] + input[i], input[i])
#     dp[1][i] = max(dp[0][i-1], dp[1][i-1] + input[i])
#
# print(max(max(dp[0]), max(dp[1])))