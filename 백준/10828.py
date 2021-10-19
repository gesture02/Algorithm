import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        stack.append(op[1])
    elif op[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif op[0] == "size":
        print(len(stack))
    elif op[0] == "empty":
        print(0) if stack else print(1)
    elif op[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)