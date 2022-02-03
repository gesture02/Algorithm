import sys
input = sys.stdin.readline

check = [0] * 2000001
def solve(sum, index):
    if index == n:
        check[sum] = 1
        return

    solve(sum+inputs[index], index+1)
    solve(sum, index+1)

n = int(input().rstrip())
inputs = list(map(int, input().split()))

solve(0, 0)

for i in range(1, 2000001):
    if not check[i]:
        print(i)
        break