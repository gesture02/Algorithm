import sys
print = sys.stdout.write
c = (
    (1, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 0, 1, 0),
    (1, 0, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 1),
    (0, 1, 1, 1, 0, 1, 0),
    (1, 1, 0, 1, 0, 1, 1),
    (1, 1, 0, 1, 1, 1, 1),
    (1, 0, 1, 0, 0, 1, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 1, 1),
)

s, n = sys.stdin.readline().split()
s = int(s)
m = len(n)
# s=1일때
for i in range(5):
    if i in [0, 2, 4]:#s==1일때 가로선의 위치
        for j in range(m):
            now = int(n[j])

            if j != 0:
                print(' ')
            print(' ')

            if (i == 0 and c[now][0]) or (i == 2 and c[now][3]) or (i == 4 and c[now][6]):
                print('-' * s)
            else:
                print(' ' * s)
            print(' ')
        print('\n')
    else:
        for l in range(s):
            for j in range(m):
                now = int(n[j])
                if j != 0:
                    print(' ')

                if (i == 1 and c[now][1]) or (i == 3 and c[now][4]):
                    print('|')
                else:
                    print(' ')
                print(' '*s)
                if (i == 1 and c[now][2]) or (i == 3 and c[now][5]):
                    print('|')
                else:
                    print(' ')
            print('\n')