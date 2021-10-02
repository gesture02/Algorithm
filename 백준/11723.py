import sys

n = int(sys.stdin.readline().rstrip())
answer = 0

for _ in range(n):
    input = sys.stdin.readline().split()
    if input[0] == 'add':
        answer = answer | (1 << int(input[1]))
    if input[0] == 'remove':
        answer = answer & ~(1 << int(input[1]))
    if input[0] == 'check':
        if answer & (1 << int(input[1])):
            print(1)
        else:
            print(0)
    if input[0] == 'toggle':
        answer = answer ^ (1 << int(input[1]))
    if input[0] == 'all':
        answer = (1 << 21) -1
    if input[0] == 'empty':
        answer = 0