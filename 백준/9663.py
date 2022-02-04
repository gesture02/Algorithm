import sys
input = sys.stdin.readline
def check(row, col):
    if checkCol[col]:
        return False
    if checkDig[row+col]:
        return False
    if checkRDig[n+row-col-1]:
        return False

    return True

def solve(row):
    if row == n:
        return 1

    answer = 0
    for col in range(n):
        if check(row, col):
            checkCol[col] = 1
            checkDig[row+col] = 1
            checkRDig[row-col+n-1] = 1
            a[row][col] = 1
            answer += solve(row+1)
            a[row][col] = 0
            checkRDig[row - col + n - 1] = 0
            checkDig[row + col] = 0
            checkCol[col] = 0
    return answer
n = int(input().rstrip())
a = [[0] * n for _ in range(n)]
checkCol = [0] * n
checkDig = [0] * (2*n-1)
checkRDig = [0] * (2*n-1)

print(solve(0))