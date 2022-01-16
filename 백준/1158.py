import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
input = deque([i+1 for i in range(n)])
result = []

while input:
    for i in range(m-1):
        input.append(input.popleft())
    result.append(input.popleft())

print('<' + ', '.join(map(str, result)) + '>')