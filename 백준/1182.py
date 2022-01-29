import sys

n, m = map(int, sys.stdin.readline().split())
inputs = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(1,  1 << n):
    sums = 0
    for j in range(n):
        if i & (1 << j):
            sums += inputs[j]

    if sums == m:
        cnt += 1

print(cnt)