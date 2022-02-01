import sys
input = sys.stdin.readline

def r1(p):
    n = len(p)
    a = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = p[n-1-i][j]

    return a
def r5(p, l):
    n = len(p)
    a = [[0] * n for _ in range(n)]
    subSize = (1 << l)
    subCount = n // subSize
    for i in range(subCount):
        for j in range(subCount):
            sx1 = i * subSize
            sy1 = j * subSize
            sx2 = (subCount-1-i) * subSize
            sy2 = j * subSize

            for x in range(subSize):
                for y in range(subSize):
                    a[sx1+x][sy1+y] = p[sx2+x][sy2+y]
    return a

def r2(p):
    n = len(p)
    a = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = p[i][n-1-j]

    return a
def r6(p, l):
    n = len(p)
    a = [[0] * n for _ in range(n)]
    subSize = (1 << l)
    subCount = n // subSize
    for i in range(subCount):
        for j in range(subCount):
            sx1 = i * subSize
            sy1 = j * subSize
            sx2 = i * subSize
            sy2 = (subCount-1-j) * subSize
            for x in range(subSize):
                for y in range(subSize):
                    a[sx1+x][sy1+y] = p[sx2+x][sy2+y]
    return a

def r3(p):
    n = len(p)
    a = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = p[n-1-j][i]

    return a
def r7(p, l):
    n = len(p)
    a = [[0] * n for _ in range(n)]
    subSize = (1 << l)
    subCount = n // subSize
    for i in range(subCount):
        for j in range(subCount):
            sx1 = i * subSize
            sy1 = j * subSize
            sx2 = (subCount-1-j) * subSize
            sy2 = i * subSize
            for x in range(subSize):
                for y in range(subSize):
                    a[sx1+x][sy1+y] = p[sx2+x][sy2+y]
    return a

def r4(p):
    n = len(p)
    a = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = p[j][n-1-i]

    return a
def r8(p, l):
    n = len(p)
    a = [[0] * n for _ in range(n)]
    subSize = (1 << l)
    subCount = n // subSize
    for i in range(subCount):
        for j in range(subCount):
            sx1 = i * subSize
            sy1 = j * subSize
            sx2 = j * subSize
            sy2 = (subCount-1-i) * subSize
            for x in range(subSize):
                for y in range(subSize):
                    a[sx1+x][sy1+y] = p[sx2+x][sy2+y]
    return a

def opOneToFour(a, k, sx, sy, length):
    tmp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            tmp[i][j] = a[sx+i][sy+j]

    if k == 1:
        tmp = r1(tmp)
    elif k == 2:
        tmp = r2(tmp)
    elif k == 3:
        tmp = r3(tmp)
    elif k == 4:
        tmp = r4(tmp)

    for i in range(length):
        for j in range(length):
            a[sx+i][sy+j] = tmp[i][j]

xx, r = map(int, input().split())
size = (1 << xx)
inputs = [list(map(int, input().split())) for _ in range(size)]

for _ in range(r):
    k, l = map(int, input().split())
    subSize = (1 << l)

    if 1 <= k <= 4:
        for i in range(0, size, subSize):
            for j in range(0, size, subSize):
                opOneToFour(inputs, k, i, j, subSize)
    elif k == 5:
        inputs = r5(inputs, l)
    elif k == 6:
        inputs = r6(inputs, l)
    elif k == 7:
        inputs = r7(inputs, l)
    elif k == 8:
        inputs = r8(inputs, l)
for i in inputs:
    print(*i)