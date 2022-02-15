import sys

MAX = 1000000

check = [True, True] + [False] * MAX
primes = []

for i in range(2, MAX+1):
    if not check[i]:
        # primes.append(i)
        j = i+i
        while j < MAX+1:
            check[j] = True
            j += i

n, m = map(int, sys.stdin.readline().split())
answer = []
for i in range(n, m+1):
    if not check[i]:
        answer.append(i)
print('\n'.join(map(str, answer)) + '\n')