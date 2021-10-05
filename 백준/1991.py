import sys
from collections import defaultdict

def preOrder(node):
    if node == '.':
        return
    print(node, end = '')
    preOrder(graph[node][0])
    preOrder(graph[node][1])
def inOrder(node):
    if node == '.':
        return
    inOrder(graph[node][0])
    print(node, end = '')
    inOrder(graph[node][1])
def postOrder(node):
    if node == '.':
        return
    postOrder(graph[node][0])
    postOrder(graph[node][1])
    print(node, end = '')

n = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)
for _ in range(n):
    a, b, c = sys.stdin.readline().split()
    graph[a].append(b)
    graph[a].append(c)

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
print()