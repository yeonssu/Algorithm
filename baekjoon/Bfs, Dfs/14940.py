import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 0 : 갈 수 없는 땅 / 1 : 갈 수 있는 땅 / 2 : 목표 지점
def bfs(start_x, start_y):
    answer = [[-1] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    que = deque()
    que.append((start_x, start_y))
    visited[start_y][start_x] = True
    answer[start_y][start_x] = 0
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1 and not visited[ny][nx]:
                answer[ny][nx] = answer[y][x] + 1
                visited[ny][nx] = True
                que.append((nx, ny))

    for wall in walls:
        answer[wall[1]][wall[0]] = 0

    for a in answer:
        print(*a)


walls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append((j, i))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(j, i)
            exit()
