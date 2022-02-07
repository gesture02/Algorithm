import sys
input = sys.stdin.readline

# def solve(index, s):
#     if index == n:
#         c[s] = 1
#         return
#
#     solve(index+1, s + inputs[index])
#     solve(index + 1, s)
#
# n = int(input().rstrip())
# inputs = list(map(int, input().split()))
# c = [0] * 2000001
# solve(0, 0)
# for i in range(1, 2000001):
#     if not c[i]:
#         print(i)
#         break

n = int(input().rstrip())
inputs = list(map(int, input().split()))
total = (1 << n)
c = [0] * 2000001
for i in range(total):
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += inputs[j]

    c[sum] = 1
for i in range(1, 2000001):
    if not c[i]:
        print(i)
        break