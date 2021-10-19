import copy
import sys
import math
from collections import deque
from itertools import combinations
from itertools import permutations
from collections import Counter
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    input = list(sys.stdin.readline().rstrip())
    sum = 0
    isTrue = True
    for i in input:
        if i == '(':
            sum += 1
        else:
            sum -= 1

        if sum < 0:
            isTrue = False
            break


    if sum > 0 or not isTrue:
        print("NO")
    elif sum == 0:
        print("YES")