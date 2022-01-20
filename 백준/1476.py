import sys

e, s, m = map(int, sys.stdin.readline().split())
E, S, M = 1, 1, 1

for i in range(1, 15*28*19 + 1):

    if e == E and s == S and m == M:
        print(i)
        break

    E += 1
    S += 1
    M += 1

    if E >= 16:
        E = 1
    if S >= 29:
        S = 1
    if M >= 20:
        M = 1