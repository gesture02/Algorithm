import sys
a = int(sys.stdin.readline().rstrip())
inputs = [0]
inputs += [int(sys.stdin.readline().rstrip()) for _ in range(a)]
dp = [[0, 0, 0] for _ in range(a+1)]

for i in range(1, a+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + inputs[i]
    dp[i][2] = dp[i-1][1] + inputs[i]
    
print(max(dp[a]))