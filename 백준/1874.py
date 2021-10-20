import sys

n = int(sys.stdin.readline().rstrip())
input = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
s = []
result = []
cnt = 1
isTrue = True
for i in input:

    while cnt <= i:
        s.append(cnt)
        result.append("+")
        cnt += 1
    if s[-1] == i:
        s.pop()
        result.append("-")
    else:
        isTrue = False
        break
if isTrue:
    for i in result:
        print(i)
else:
    print("NO")