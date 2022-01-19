import sys
shapes = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],   #ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],   #ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],   #ㅣ
    [(0, 0), (1, 0), (1, 1), (1, 2)],   #ㄴ
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],   #ㄱ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],   #ㄴ 세운거
    [(0, 1), (1, 1), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],   #ㄱ
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 1), (1, 0), (1, 1), (2, 0)],   #ㄹ?
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],   #ㅜ
    [(1, 0), (0, 1), (1, 1), (1, 2)],   #ㅗ
    [(0, 1), (1, 0), (1, 1), (2, 1)],   #ㅓ
    [(0, 0), (1, 0), (1, 1), (2, 0)]    #ㅏ
]

def check(x, y):
    answer = 0

    for i in range(19):
        cnt = 0
        for j in range(4):
            a, b = shapes[i][j][0], shapes[i][j][1]
            if x + a < n and y + b < m:
                cnt += inputs[x + a][y + b]

        if answer < cnt:
            answer = cnt

    return answer

n, m = map(int, sys.stdin.readline().split())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        cnt = check(i, j)
        if answer < cnt:
            answer = cnt

print(answer)