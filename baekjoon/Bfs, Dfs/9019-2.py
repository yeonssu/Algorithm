import sys
from collections import deque

input = sys.stdin.readline
T = int(input().strip())
for t in range(T):
    a, b = map(int, input().strip().split())
    que = deque()
    que.append((a, ""))
    visited = [False for _ in range(10001)]

    while que:
        num, result = que.popleft()
        visited[num] = True
        if num == b:
            print(result)
            break

        num1 = (num * 2) % 10000
        if not visited[num1]:
            que.append((num1, result + "D"))
            visited[num1] = True

        num2 = (num - 1) % 10000
        if not visited[num2]:
            que.append((num2, result + "S"))
            visited[num2] = True

        num3 = (10 * num + (num // 1000)) % 10000
        if not visited[num3]:
            que.append((num3, result + "L"))
            visited[num3] = True

        num4 = (num // 10 + (num % 10) * 1000) % 10000
        if not visited[num4]:
            que.append((num4, result + "R"))
            visited[num4] = True
