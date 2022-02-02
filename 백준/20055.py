import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
box = [0] * (2*n)
l = len(a)
cnt = 0
tryCnt = 1

while True:

    # a = a[-1:] + a[:-1]
    # box = box[-1:] + box[:-1]

    tmp = a[l - 1]
    for i in range(l - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = tmp
    tmp = box[l - 1]
    for i in range(l - 1, 0, -1):
        box[i] = box[i - 1]
    box[0] = tmp

    if box[n-1]:
        box[n-1] = 0

    for i in range(l-2, -1, -1):
        if box[i]:
            if box[i+1] == 0 and a[i+1] > 0:
                box[i+1] = 1
                box[i] = 0
                a[i+1] -= 1
                if a[i+1] == 0:
                    cnt += 1
    if box[n-1]:
        box[n-1] = 0

    if a[0] > 0:
        box[0] = 1
        a[0] -= 1
        if a[0] == 0:
            cnt += 1

    if cnt >= k:
        print(tryCnt)
        break

    tryCnt += 1