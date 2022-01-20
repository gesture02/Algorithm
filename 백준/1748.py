import sys

n = int(sys.stdin.readline().rstrip())

start = 1
length = 1
answer = 0

while start <= n:
    end = start * 10 - 1
    if end > n:
        end = n
    answer += (end - start + 1) * length
    start *= 10
    length += 1

print(answer)