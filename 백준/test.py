import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = int(input().rstrip())
c = [[0] * 101 for _ in range(101)]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    c[x][y] = 1
    dir = [d]

    for i in range(1, g+1):
        tmp = dir[:]
        tmp = tmp[::-1]

        for j in range(len(tmp)):
            tmp[j] = (tmp[j] + 1) % 4

        dir += tmp

    for d in dir:
        x += dx[d]
        y += dy[d]
        c[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if c[i][j] and c[i+1][j] and c[i][j+1] and c[i+1][j+1]:
            cnt += 1

print(cnt)