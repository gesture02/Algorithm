import sys
input = sys.stdin.readline

def solve(x1, y1, x2, y2, step):
    if step == 11: return -1
    fall1, fall2 = False, False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        fall2 = True
    if fall1 and fall2: return -1
    if fall1 or fall2: return step

    answer = -1
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]

        if 0 <= nx1 < n and 0 <= ny1 < m and inputs[nx1][ny1] == '#':
            nx1 = x1
            ny1 = y1

        if 0 <= nx2 < n and 0 <= ny2 < m and inputs[nx2][ny2] == '#':
            nx2 = x2
            ny2 = y2

        temp = solve(nx1, ny1, nx2, ny2, step+1)
        if temp == -1: continue
        if answer == -1 or answer > temp:
            answer = temp

    return answer

n, m = map(int, input().split())
inputs = [list(input().rstrip()) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
check = [[0] * m for _ in range(n)]
coins = [[i, j] for i in range(n) for j in range(m) if inputs[i][j] == 'o']
sx1, sy1, sx2, sy2 = coins[0][0], coins[0][1], coins[1][0], coins[1][1]
inputs[sx1][sy1] = '.'
inputs[sx2][sy2] = '.'
print(solve(sx1, sy1, sx2, sy2, 0))