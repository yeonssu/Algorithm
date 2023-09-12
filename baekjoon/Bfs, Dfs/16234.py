import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y):
    que = deque()
    que.append((start_x, start_y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = [(start_x, start_y)]
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and L <= abs(country[y][x] - country[ny][nx]) <= R and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((nx, ny))
                temp.append((nx, ny))

    return temp


if __name__ == "__main__":
    N, L, R = map(int, input().strip().split())
    country = [list(map(int, input().strip().split())) for _ in range(N)]
    day = 0
    flag = True
    while flag:
        visited = [[False] * N for _ in range(N)]
        flag = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    union = bfs(j, i)
                    if len(union) > 1:
                        flag = True
                        div = sum([country[y][x] for x, y in union]) // len(union)
                        for x, y in union:
                            country[y][x] = div
        if not flag:
            break
        day += 1
    print(day)
