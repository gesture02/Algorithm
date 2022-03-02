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
def permutation(c):
    global answer

    while True:
        if c[0] != 0: break
        ok = True
        s = 0
        for i in range(len(c)-1):
            if inputs[c[i]][c[i+1]] == 0:
                ok = False
                break
            else:
                s += inputs[c[i]][c[i+1]]

        if ok and inputs[c[-1]][c[0]] != 0:
            s += inputs[c[-1]][c[0]]
            if answer > s:
                answer = s

        if not nextPermutation(c): break
n = int(sys.stdin.readline().rstrip())
inputs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
city = [i for i in range(n)]
answer = sys.maxsize
permutation(city)
print(answer)

# def dfs(path, nextx, cnt):
#     global minv
#
#     lastx = path[-1]
#     if len(path) == n:
#         startx = path[0]
#         if input[lastx][startx] != 0:
#             minv = min(minv, cnt + input[lastx][startx])
#         return
#
#     for i in range(n):
#         if not visited[i] and input[nextx][i] != 0:
#             visited[i] = 1
#             path.append(i)
#             dfs(path, i, cnt + input[nextx][i])
#             visited[i] = 0
#             path.pop()
#
#
# n = int(sys.stdin.readline().rstrip())
# input = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# visited = [0] * n
# minv = sys.maxsize
#
# visited[0] = 1
# dfs([0], 0, 0)
#
# print(minv)