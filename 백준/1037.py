import sys

n = int(sys.stdin.readline().rstrip())
m = list(map(int, sys.stdin.readline().split()))

print(max(m) * min(m))