import sys

while True:
    try:
        n: int = int(sys.stdin.readline().rstrip())
        answer = 1
        cnt = 1
        while True:
            if not answer % n:
                break
            answer = (answer % n) * 10 + 1
            cnt += 1

        print(cnt)
    except:
        break