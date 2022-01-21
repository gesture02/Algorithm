import sys

def solve(index):
    if index == m:
        sys.stdout.write(' '.join(map(str, answer)) + '\n')
        return

    for i in range(1, n+1):
        answer[index] = i
        solve(index+1)

n, m = map(int, sys.stdin.readline().split())
answer = [0] * m

solve(0)