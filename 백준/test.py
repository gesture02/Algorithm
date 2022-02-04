import sys
input = sys.stdin.readline

def check(index, p, k):
    if inputs[index] == '<':
        if p[-1] > k:
            return False
    else:
        if p[-1] < k:
            return False

    return True

def solve(index, p):
    if index == n+1:
        result.append(''.join(map(str, p)))
        return

    for i in range(10):
        if c[i]: continue
        if index == 0 or check(index-1, p, i):
            c[i] = 1
            solve(index+1, p+[i])
            c[i] = 0

n =  int(input().rstrip())
inputs = list(input().split())
c = [0] * 10
result = []
solve(0, [])
result.sort()
print(result[-1])
print(result[0])
