import sys

def solve(index, start):
    if index == m:
        sys.stdout.write(' '.join(map(str, answer)) + '\n')
        return

    for i in range(start+1, n+1):
        answer[index] = i
        solve(index+1, i)

n, m = map(int, sys.stdin.readline().split())
answer = [0] * m

solve(0, 0)