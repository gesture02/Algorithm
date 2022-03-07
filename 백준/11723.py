import sys

n = int(sys.stdin.readline().rstrip())
answer = 0

for _ in range(n):
    op = list(sys.stdin.readline().split())
    if op[0] == 'add':
        answer = answer | (1 << int(op[1]))
    elif op[0] == 'remove':
        answer = answer & ~(1 << int(op[1]))
    elif op[0] == 'check':
        if answer & (1 << int(op[1])):
            print(1)
        else:
            print(0)
    elif op[0] == 'toggle':
        answer = answer ^ (1 << int(op[1]))
    elif op[0] == 'all':
        answer = (1 << 21) - 1
    elif op[0] == 'empty':
        answer = 0