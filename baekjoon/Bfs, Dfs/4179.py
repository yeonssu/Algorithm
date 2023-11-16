import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y):
    que = deque()
    que.append((start_x, start_y))
    visited = [[0] * c for _ in range(r)]
    visited[start_y][start_x] = 1
    while fire:
        x, y = fire.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r and not visited_fire[ny][nx] and graph[ny][nx] != "#":
                visited_fire[ny][nx] = visited_fire[y][x] + 1
                fire.append((nx, ny))

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r:
                if (not visited[ny][nx] and graph[ny][nx] != "#"
                        and (not visited_fire[ny][nx] or visited[y][x] + 1 < visited_fire[ny][nx])):
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((nx, ny))

            else:
                    return visited[y][x]

    return "IMPOSSIBLE"


if __name__ == "__main__":
    r, c = map(int, input().strip().split())
    graph = [list(map(str, input().strip())) for _ in range(r)]
    visited_fire = [[0] * c for _ in range(r)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start = (0, 0)
    fire = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "J":
                start = (j, i)
            elif graph[i][j] == "F":
                fire.append((j, i))
                visited_fire[i][j] = 1
    print(bfs(start[0], start[1]))
