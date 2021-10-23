import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

d = deque()

for _ in range(n):
    input = sys.stdin.readline().split()

    if input[0] == 'push':
        d.append(input[1])
    elif input[0] == 'pop':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif input[0] == 'size':
        print(len(d))
    elif input[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif input[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif input[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)