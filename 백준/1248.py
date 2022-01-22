import sys

def check(index):
    sums = 0
    for i in range(index, -1, -1):
        sums += answer[i]
        if s[i][index] > 0:
            if sums <= 0:
                return False
        elif s[i][index] == 0:
            if sums != 0:
                return False
        elif s[i][index] < 0:
            if sums >= 0:
                return False
    return True

def solve(index):
    if index == n:
        return True

    if s[index][index] == 0:
        answer[index] = 0
        return check(index) and solve(index+1)

    for i in range(1, 11):
        answer[index] = s[index][index] * i
        if check(index) and solve(index + 1):
            return True

    return False

n = int(sys.stdin.readline().rstrip())
inputs = list(sys.stdin.readline().rstrip())
s = [[0] * n for _ in range(n)]
answer = [0] * n
cnt = 0

for i in range(n):
    for j in range(i, n):
        tmp = inputs[cnt]
        if tmp == '+':
            s[i][j] = 1
        elif tmp == '-':
            s[i][j] = -1
        else:
            s[i][j] = 0
        cnt += 1
solve(0)
print(*answer)