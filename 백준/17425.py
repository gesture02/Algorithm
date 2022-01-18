import sys
MAX = 1000001

f = [1] * MAX
g = [0] * MAX
for i in range(2, MAX):
    j = 1
    while i*j < MAX:
        f[i * j] += i
        j += 1

for i in range(1, MAX):
    g[i] = g[i - 1] + f[i]

answer = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    answer.append(g[m])

print('\n'.join(map(str, answer)) + '\n')
