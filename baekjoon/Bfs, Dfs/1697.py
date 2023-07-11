import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().strip().split())
distance = [0] * (10 ** 5 + 1)
visited = [False] * (10 ** 5 + 1)


def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        x = que.popleft()
        if x == K:
            print(distance[x])
            exit()

        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 10 ** 5 and not visited[nx]:
                que.append(nx)
                visited[nx] = True
                distance[nx] = distance[x] + 1


bfs(N)
