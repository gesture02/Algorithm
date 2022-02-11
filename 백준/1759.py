import sys
def moJaCheck(pwd):
    mo, ja = 0, 0
    for i in pwd:
        if i in 'aeiou':
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2

def solve(pwd, index):
    if len(pwd) == n:
        if moJaCheck(pwd):
            answer.append(''.join(map(str, pwd)))
        return

    if len(pwd) != n and index == m:
        return

    solve(pwd + [alpha[index]], index + 1)
    solve(pwd, index+1)

n, m = map(int, sys.stdin.readline().split())
alpha = list(sys.stdin.readline().split())
check = [0] * m
answer = []
alpha.sort()

solve([], 0)

print('\n'.join(map(str, answer)))