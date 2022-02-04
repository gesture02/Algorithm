import sys

# def ok(numbers, num, index):
#     if inputs[index] == '<':
#         if numbers[-1] > num:
#             return False
#     if inputs[index] == '>':
#         if numbers[-1] < num:
#             return False
#
#     return True
#
# def solve(numbers, index):
#     if index == n+1:
#         answer.append(''.join(map(str, numbers)))
#         return
#
#     for i in range(10):
#         if check[i]: continue
#         check[i] = 1
#         if index == 0 or ok(numbers, i, index-1):
#             solve(numbers+[i], index+1)
#         check[i] = 0
#
#
# n = int(sys.stdin.readline().rstrip())
# inputs = list(sys.stdin.readline().split())
# check = [0] * 10
# answer = []
#
# solve([], 0)
#
# print(answer[-1])
# print(answer[0])

def nextPermutation(p):
    i = len(p) - 1
    while i > 0 and p[i-1] >= p[i]:
        i -= 1
    if i <= 0: return False
    j = len(p)-1
    while p[i-1] >= p[j]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]
    j = len(p)-1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    return True

def prevPermutation(p):
    i = len(p) - 1
    while i > 0 and p[i-1] <= p[i]:
        i -= 1
    if i <= 0: return False
    j = len(p)-1
    while p[i-1] <= p[j]:
        j -= 1
    p[i-1], p[j] = p[j], p[i-1]
    j = len(p)-1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1
    return True

def check(p):
    for i in range(n):
        if inputs[i] == '<':
            if p[i] > p[i+1]:
                return False
        else:
            if p[i] < p[i+1]:
                return False
    return True
n = int(sys.stdin.readline().rstrip())
inputs = list(sys.stdin.readline().split())

a = [i for i in range(9, 9-n-1, -1)]
b = [i for i in range(n+1)]

while True:
    if check(a):
        print(''.join(map(str, a)))
        break
    if not prevPermutation(a):
        break
while True:
    if check(b):
        print(''.join(map(str, b)))
        break
    if not nextPermutation(b):
        break