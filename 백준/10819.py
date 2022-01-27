import sys

def nextPermutation(p):
    i = n-1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    if i <= 0: return False
    j = n-1
    while p[i-1] >= p[j]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]
    j = n-1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    return True

def permutation(inputs):
    global answer
    s = 0
    for i in range(n - 1):
        s += abs(inputs[i] - inputs[i + 1])
    answer = s
    while nextPermutation(inputs):
        s = 0
        for a in range(n - 1):
            s += abs(inputs[a] - inputs[a + 1])
        if answer < s:
            answer = s
n = int(sys.stdin.readline().rstrip())
inputs = list(map(int, sys.stdin.readline().split()))
answer = -sys.maxsize
inputs.sort()

permutation(inputs)
print(answer)