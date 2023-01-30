from collections import deque

N = int(input())
graph = []
for n in range(N):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False] * N for _ in range(N)]


def bfs(a, b):
    que = deque([[a, b]])
    visited[a][b] = True
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            # 이거 왜 안돼?

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = True
                    que.append([nx, ny])


cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

cntRGB = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = "G"

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cntRGB += 1

print(cnt, cntRGB)
