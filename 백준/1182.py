import sys

def solve(sum, index):
    global cnt

    if index == n:
        if sum == m:
            cnt += 1
        return

    solve(sum+inputs[index], index+1)
    solve(sum, index+1)


n, m = map(int, sys.stdin.readline().split())
inputs = list(map(int, sys.stdin.readline().split()))
cnt = 0
# for i in range(1,  1 << n):
#     sums = 0
#     for j in range(n):
#         if i & (1 << j):
#             sums += inputs[j]
#
#     if sums == m:
#         cnt += 1
#print(cnt)

solve(0, 0)
print(cnt-1 if m == 0 else cnt)