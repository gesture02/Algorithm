import sys

# def solve(index, start):
#     if index == m:
#         sys.stdout.write(' '.join(map(str, answer)) + '\n')
#         return
#
#     for i in range(start+1, n+1):
#         answer[index] = i
#         solve(index+1, i)
#
# n, m = map(int, sys.stdin.readline().split())
# answer = [0] * m
#
# solve(0, 0)

## 선택으로 풀기

def solve(p, index):
    if len(p) == m:
        print(*p)
        return

    if len(p) != m and index == n:
        return

    solve(p + [inputs[index]], index+1)
    solve(p, index+1)


n, m = map(int, sys.stdin.readline().split())
inputs = [i+1 for i in range(n)]
solve([], 0)