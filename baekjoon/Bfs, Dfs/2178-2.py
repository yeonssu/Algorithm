import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = []
for n in range(N):
    graph.append(list(map(int, input().strip())))

answer = []


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited = [[False] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] != 0:
                graph[ny][nx] = graph[y][x] + 1
                visited[ny][nx] = True
                que.append((nx, ny))


bfs(0, 0)
print(graph[N - 1][M - 1])
