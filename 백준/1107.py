import sys

def check(number):
    n = str(number)
    for i in n:
        if i in inputs:
            return False
    return True

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
inputs = list(sys.stdin.readline().split())

result = abs(n - 100)

for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i-n))

print(result)





















# def check(num):
#     num = str(num)
#     for i in num:
#         if int(i) in inputs:
#             return False
#     return True
#
# result = abs(n - 100)
#
# for i in range(1000001):
#     if check(i):
#         result = min(result, len(str(i)) + abs(i - n))
#
# print(result)