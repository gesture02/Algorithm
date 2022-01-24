import sys

def solve(index):
    if index == m:
        sys.stdout.write(' '.join(map(str, answer)) + '\n')
        return

    for i in range(len(inputs)):
        if check[i]: continue
        check[i] = 1
        answer[index] = inputs[i]
        solve(index+1)
        check[i] = 0

n, m = map(int, sys.stdin.readline().split())
inputs = list(map(int, sys.stdin.readline().split()))
inputs.sort()

check = [0] * (n+1)
answer = [0] * m

solve(0)