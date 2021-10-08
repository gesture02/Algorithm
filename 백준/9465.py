import sys

l = int(sys.stdin.readline().rstrip())

for _ in range(l):
    n = int(sys.stdin.readline().rstrip())
    input = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    if n == 1:
        print(max(input[0][0], input[1][0]))
        continue
    input[0][1] += input[1][0]
    input[1][1] += input[0][0]

    for i in range(2, n):
        input[0][i] += max(input[1][i-1], input[1][i-2])
        input[1][i] += max(input[0][i-1], input[0][i-2])

    print(max(input[0][n-1], input[1][n-1]))