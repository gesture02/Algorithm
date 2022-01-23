import sys

def solve():
    global answer
    for case in range(1 << (n*m)):
        sum = 0

        for i in range(n):
            number = 0
            for j in range(m):
                cur = i*m+j
                if case & (1 << cur) == 0:
                    number = number * 10 + inputs[i][j]
                else:
                    sum += number
                    number = 0
            sum += number
        for j in range(m):
            number = 0
            for i in range(n):
                cur = i*m+j
                if case & (1 << cur) != 0:
                    number = number * 10 + inputs[i][j]
                else:
                    sum += number
                    number = 0
            sum += number
        if answer < sum:
            answer = sum

n, m = map(int, sys.stdin.readline().split())
inputs = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
answer = 0

solve()
print(answer)