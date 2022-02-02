import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]
size = min(n, m) // 2

for k in range(size):
    a = []
    for j in range(k, m-k):
        a.append(inputs[k][j])
    for i in range(k+1, n-k):
        a.append(inputs[i][m-1-k])
    for j in range(m-2-k, k-1, -1):
        a.append(inputs[n-1-k][j])
    for i in range(n-2-k, k, -1):
        a.append(inputs[i][k])

    l = len(a)
    index = r % l

    for j in range(k, m-k):
        inputs[k][j] = a[index]
        index = (index+1) % l
    for i in range(k+1, n-k):
        inputs[i][m-1-k] = a[index]
        index = (index+1) % l
    for j in range(m-2-k, k-1, -1):
        inputs[n - 1 - k][j] = a[index]
        index = (index + 1) % l
        a.append(inputs[n-1-k][j])
    for i in range(n-2-k, k, -1):
        inputs[i][k] = a[index]
        index = (index + 1) % l

for i in inputs:
    print(*i)