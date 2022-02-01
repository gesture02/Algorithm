import sys

n, m = map(int, sys.stdin.readline().split())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = n*m*2

for i in range(n):
    answer += inputs[i][0]
    diff = 0
    for j in range(1, m):
        if inputs[i][j-1] < inputs[i][j]:
            diff += inputs[i][j] - inputs[i][j-1]
    answer += diff
for i in range(n):
    answer += inputs[i][m-1]
    diff = 0
    for j in range(m-2, -1, -1):
        if inputs[i][j] > inputs[i][j+1]:
            diff += inputs[i][j] - inputs[i][j+1]
    answer += diff
for i in range(m):
    answer += inputs[0][i]
    diff = 0
    for j in range(1, n):
        if inputs[j-1][i] < inputs[j][i]:
            diff += inputs[j][i] - inputs[j-1][i]
    answer += diff
for i in range(m):
    answer += inputs[n-1][i]
    diff = 0
    for j in range(n-2, -1, -1):
        if inputs[j][i] > inputs[j+1][i]:
            diff += inputs[j][i] - inputs[j+1][i]
    answer += diff

print(answer)