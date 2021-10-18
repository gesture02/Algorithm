import sys

def check(idx):
    sums = 0
    for i in range(idx, -1, -1):
        sums += result[i]
        if sums == 0 and S[i][idx] != 0:
            return False
        elif sums > 0 and S[i][idx] <= 0:
            return False
        elif sums < 0 and S[i][idx] >= 0:
            return False
    return True

def answer(depth):
    global result

    if depth == n:
        return True

    if S[depth][depth] == 0:
        result[depth] = 0
        return answer(depth+1)

    for i in range(1, 11):
        result[depth] = S[depth][depth] * i
        if check(depth) and answer(depth+1):
            return True
    return False


n = int(sys.stdin.readline().rstrip())
input = list(sys.stdin.readline().rstrip())
S = [[0] * n for _ in range(n)]
result = [0] * n

for i in range(n):
    for j in range(i, n):
        temp = input.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

answer(0)
print(*result)