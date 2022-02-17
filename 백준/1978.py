import sys

MAX = 1000000

check = [True, True] + [False] * MAX
primes = []

for i in range(2, MAX+1):
    if not check[i]:
        primes.append(i)
        j = i+i

        while j < MAX+1:
            check[j] = True
            j += i

n = int(sys.stdin.readline().rstrip())
inputs = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in inputs:
    if not check[i]:
        cnt += 1
print(cnt)