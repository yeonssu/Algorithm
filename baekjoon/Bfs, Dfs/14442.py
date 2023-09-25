import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y, k):
    que = deque()
    que.append((start_x, start_y, k))
    visited = [[[0] * K for _ in range(M)] for _ in range(N)]
    visited[start_y][start_x][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while que:
        x, y, k = que.popleft()
        if x == M - 1 and y == N - 1:
            return visited[y][x]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and k > 0 and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((nx, ny, k - 1))
                elif graph[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((nx, ny, k))
    return -1


if __name__ == "__main__":
    N, M, K = map(int, input().strip().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    print(bfs(0, 0, K))
