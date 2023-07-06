import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
# O : 빈 공간 / X : 벽 / I : 도연이 / P : 사람
graph = [list(map(str, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, cnt):
    que = deque()
    que.append((x, y))
    visited[y][x] = True
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if graph[ny][nx] == "O":
                    que.append((nx, ny))
                elif graph[ny][nx] == "P":
                    cnt += 1
                    que.append((nx, ny))
                visited[ny][nx] = True
    return cnt


for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            cnt = bfs(j, i, 0)
            break
if cnt == 0:
    print("TT")
else:
    print(cnt)
