import sys

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n, m = map(int, sys.stdin.readline().split())

GCD = gcd(n, m)
LCM = n*m // GCD
print(GCD)
print(LCM)