import sys
input = sys.stdin.readline

def check(i, j, value):
    if checkRow[i][value]:
        return False
    if checkCol[j][value]:
        return False
    block = 3 * (i // 3) + j // 3
    if check3x3[block][value]:
        return False

    return True

def solve(z):
    if z == 81:
        for row in a:
            print(*row)
        return True

    x, y = z//n, z%n
    if a[x][y] != 0:
        return solve(z+1)
    for i in range(1, 10):
        if check(x, y, i):
            checkRow[x][i] = 1
            checkCol[y][i] = 1
            block = 3 * (x//3) + y//3
            check3x3[block][i] = 1
            a[x][y] = i
            if solve(z+1):
                return True
            a[x][y] = 0
            check3x3[block][i] = 0
            checkCol[y][i] = 0
            checkRow[x][i] = 0
    return False


a = [list(map(int, input().split())) for _ in range(9)]
n = 9
checkRow = [[0] * 10 for _ in range(9)]
checkCol = [[0] * 10 for _ in range(9)]
check3x3 = [[0] * 10 for _ in range(9)]
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            checkRow[i][a[i][j]] = 1
            checkCol[j][a[i][j]] = 1
            b = 3 * (i//3) + j//3
            check3x3[b][a[i][j]] = 1
solve(0)