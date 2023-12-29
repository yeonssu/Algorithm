import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    que = deque(enumerate(map(int, input().strip().split())))
    answer = []
    while que:
        idx, num = que.popleft()
        answer.append(idx + 1)
        if num > 0:
            que.rotate(-(num - 1))
        else:
            que.rotate(-num)

    print(*answer)