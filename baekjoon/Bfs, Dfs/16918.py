import sys
from collections import deque
input = sys.stdin.readline

def install():
    que = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "O":
                que.append((j, i))
            else:
                graph[i][j] = "O"
    return que

def boom(q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        graph[y][x] = "."
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= ny < R and 0 <= nx < C:
                graph[ny][nx] = "."


if __name__ == "__main__":
    R, C, N = map(int, input().strip().split())
    graph = [list(map(str, input().strip())) for _ in range(R)]
    for n in range(N + 1):
        if n % 3 == 0:
            continue
        elif n % 3 == 1:
            q = install()
        elif n % 3 == 2:
            boom(q)
    for gra in graph:
        answer = ""
        for g in gra:
            answer += g
        print(answer)




