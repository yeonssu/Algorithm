import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = []
for n in range(N):
    graph.append(list(map(int, input().strip().split())))


def bfs():
    que = deque()
    que.append((0, 0))
    visited[0][0] = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    que.append((nx, ny))


time = 0
while True:
    visited = [[False] * M for _ in range(N)]
    bfs()
    change = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                change = True
            elif graph[i][j] == 2:
                graph[i][j] = 1

    if change:
        time += 1
    else:
        break

print(time)
