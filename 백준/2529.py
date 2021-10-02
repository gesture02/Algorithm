import sys
def dfs(s, depth):
    global result
    if len(s) == n+1:
        result.append(''.join(map(str, s)))
        return
    for i in range(10):
        if not visited[i]:
            if input[depth] == '<':
                if s[-1] > i:
                    continue
            if input[depth] == '>':
                if s[-1] < i:
                    continue
            visited[i] = 1
            s.append(i)
            dfs(s, depth+1)
            visited[i] = 0
            s.pop()

n = int(sys.stdin.readline().rstrip())
input = list(sys.stdin.readline().split())
visited = [0] * 10
result = []

for i in range(10):
    visited[i] = 1
    dfs([i], 0)
    visited[i] = 0

print(result[-1])
print(result[0])
