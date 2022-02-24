import sys

inputs = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
inputs.sort()
s = sum(inputs)

for i in range(9):
    for j in range(i+1, 9):
        if s - (inputs[i]+inputs[j]) == 100:
            for k in range(9):
                if i == k or j == k: continue
                print(inputs[k])
            sys.exit(0)