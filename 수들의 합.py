# import collections
# import itertools
# import math
import sys
# from collections import deque
# from collections import defaultdict
# sys.setrecursionlimit(100000)

n = int(sys.stdin.readline().rstrip())
sums = 0
cnt = 0
while sums <= n:
    cnt += 1
    sums = cnt * (cnt + 1) // 2

print(cnt-1)