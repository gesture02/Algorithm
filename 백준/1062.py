import sys
input = sys.stdin.readline

def count(mask, words):
    cnt = 0
    for word in words:
        if word & ((1 << 26) - 1 - mask) == 0:
            cnt += 1
    return cnt

def solve(index, k, mask, words):
    if k < 0:
        return -1
    if index == 26:
        return count(mask, words)
    answer = 0
    t1 = solve(index+1, k-1, mask | (1 << index), words)
    if answer < t1:
        answer = t1
    if index not in [ord('a') - ord('a'), ord('n') - ord('a'), ord('t') - ord('a'), ord('i') - ord('a'), ord('c') - ord('a')]:
        t2 = solve(index+1, k, mask, words)
        if answer < t2:
            answer = t2

    return answer

n, k = map(int, input().split())
words = [0] * n
for i in range(n):
    word = input().rstrip()
    for w in word:
        words[i] = words[i] | (1 << (ord(w)-ord('a')))

print(solve(0, k, 0, words))