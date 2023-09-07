import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y, complex):
    que = deque()
    que.append((start_x, start_y))
    visited[start_y][start_x] = complex
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = complex
                que.append((nx, ny))

    cnt = 0
    for v in visited:
        cnt += v.count(complex)
    return cnt


if __name__ == "__main__":
    N = int(input().strip())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    complex = 1
    answer = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] == 1:
                answer.append(bfs(j, i, complex))
                complex += 1
    print(complex - 1)
    answer.sort()
    for a in answer:
        print(a)
