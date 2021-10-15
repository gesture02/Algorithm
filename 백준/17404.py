import sys

n = int(sys.stdin.readline().rstrip())
input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = sys.maxsize

for color in range(3):
    dp = [[0, 0, 0] for _ in range(n)]

    for i in range(3):
        if color == i:
            dp[0][i] = input[0][i]
            continue
        dp[0][i] = sys.maxsize

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + input[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + input[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + input[i][2]

    for i in range(3):
        if color == i:
            continue
        result = min(result, dp[n-1][i])

print(result)