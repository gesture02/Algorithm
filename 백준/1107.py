import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
input = list(map(int, sys.stdin.readline().split()))

def check(num):
    num = str(num)
    for i in num:
        if int(i) in input:
            return False
    return True

result = abs(n - 100)

for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i - n))

print(result)