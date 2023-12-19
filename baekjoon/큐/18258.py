import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    que = deque()
    for _ in range(n):
        word = input().strip()
        if word[-1].isdigit():
            word, num = word.split()

        if word == 'push':
            que.append(num)
        elif word == 'pop':
            if len(que) > 0:
                print(que.popleft())
            else:
                print(-1)
        elif word == 'size':
            print(len(que))
        elif word == 'empty':
            if len(que) > 0:
                print(0)
            else:
                print(1)
        elif word == 'front':
            if len(que) > 0:
                print(que[0])
            else:
                print(-1)
        elif word == 'back':
            if len(que) > 0:
                print(que[-1])
            else:
                print(-1)
