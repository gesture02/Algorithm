import sys

s1 = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
s2 = []
for i in range(n):
    input = sys.stdin.readline().split()
    if input[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif input[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif input[0] == 'B':
        if s1:
            s1.pop()
    elif input[0] == 'P':
        a = input[1]
        s1.append(a)

print(''.join(s1 + list(reversed(s2))))