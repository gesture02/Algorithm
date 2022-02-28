import sys

def check(r1, r2, c1, c2):
    answer = 1

    for i in range(r1, r2+1):
        cnt = 1
        for j in range(n-1):

            if inputs[i][j] == inputs[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            if answer <= cnt:
                answer = cnt

    for i in range(c1, c2+1):
        cnt = 1
        for j in range(n-1):

            if inputs[j][i] == inputs[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            if answer <= cnt:
                answer = cnt

    return answer

n = int(sys.stdin.readline().rstrip())
inputs = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        if i < n-1:
            inputs[i][j], inputs[i + 1][j] = inputs[i + 1][j], inputs[i][j]
            cnt = check(i, i + 1, j, j)
            if answer < cnt:
                answer = cnt
            inputs[i][j], inputs[i + 1][j] = inputs[i + 1][j], inputs[i][j]

        if j < n-1:
            inputs[i][j], inputs[i][j + 1] = inputs[i][j + 1], inputs[i][j]
            cnt = check(i, i, j, j + 1)
            if answer < cnt:
                answer = cnt
            inputs[i][j], inputs[i][j + 1] = inputs[i][j + 1], inputs[i][j]

print(answer)