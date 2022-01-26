import sys

n = int(sys.stdin.readline().rstrip())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n-1):
    inputs[i+1][0] += inputs[i][0]
    inputs[i+1][i+1] += inputs[i][i]
    for j in range(1, i+1):
        inputs[i+1][j] += max(inputs[i][j-1], inputs[i][j])
print(max(inputs[n-1]))