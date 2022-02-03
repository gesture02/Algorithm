import sys
input = sys.stdin.readline

def check(a, l):
    c = [0] * n

    for i in range(1, n):
        if a[i-1] != a[i]:
            diff = abs(a[i]-a[i-1])
            if diff != 1:
                return False

            if a[i-1] < a[i]:
                for j in range(1, l+1):
                    if i-j < 0: return False
                    if a[i-1] != a[i-j]: return False
                    if c[i-j]: return False
                    c[i-j] = 1

            elif a[i-1] > a[i]:
                for j in range(l):
                    if i+j >= n: return False
                    if a[i] != a[i+j]: return False
                    if c[i+j]: return False
                    c[i+j] = 1
    return True

n, l = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    a = inputs[i][:]
    if check(a, l):
        cnt += 1

for i in range(n):
    a = []
    for j in range(n):
        a.append(inputs[j][i])
    if check(a, l):
        cnt += 1
print(cnt)