import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y, k):
    que = deque()
    que.append((start_x, start_y, k))
    visited = [[False] * M for _ in range(N)]
    visited[start_y][start_x] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while que:
        x, y, k = que.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and k > 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((nx, ny, k - 1))
                elif graph[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((nx, ny, k))


if __name__ == "__main__":
    N, M, K = map(int, input().strip().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    print(graph)
    bfs(0, 0, K)
