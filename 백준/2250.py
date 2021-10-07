import sys
sys.setrecursionlimit(100000)
def inOrder(node, prev):
    if node == -1: return
    levels[node] = levels[prev] + 1
    inOrder(graph[node][0], node)
    inOrder(graph[node][1], node)

def answer(node):
    global cnt
    if node == -1: return
    answer(graph[node][0])
    cnt += 1
    arrays[levels[node]][cnt] = node
    answer(graph[node][1])

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
findRoot = [0] * (n+1)
for _ in range(n):
    root, left, right = map(int, sys.stdin.readline().split())
    graph[root].append(left)
    graph[root].append(right)

    findRoot[root] += 1
    if left != -1:
        findRoot[left] += 1
    if right != -1:
        findRoot[right] += 1
root = 0
for i in range(len(findRoot)):
    if findRoot[i] == 1:
        root = i
levels = [0] * (n+1)
cnt = 0
inOrder(root, 0)
arrays = [[0] * (n+1) for _ in range(max(levels) + 1)]
answer(root)
result = [0, 0]
for i in range(1, max(levels)+1):
    idx1 = 0
    idx2 = 0
    for j in range(1, n+1):
        if arrays[i][j] != 0:
            idx1 = j-1
            break
    for j in range(n, 0, -1):
        if arrays[i][j] != 0:
            idx2 = j
            break
    if result[1] < idx2 - idx1:
        result = [i, idx2 - idx1]

print(*result)