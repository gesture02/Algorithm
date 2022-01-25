import sys

# n = int(sys.stdin.readline().rstrip())
# input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dp = [0] * (n+1)
# for i in range(n-1, -1, -1):
#     if i + input[i][0] > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(dp[i + 1], input[i][1] + dp[i + input[i][0]])
#
# print(max(dp))


#재귀로 풀기

def solve(day, money):
    global answer

    if day == n:
        if answer < money:
            answer = money
        return
    if day > n:
        return

    solve(day+inputs[day][0], money+inputs[day][1])
    solve(day+1, money)
n = int(sys.stdin.readline().rstrip())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

solve(0, 0)

print(answer)