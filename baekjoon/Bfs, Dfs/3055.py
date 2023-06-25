import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().strip().split())

graph = [list(input().strip()) for _ in range(R)]
def print_graph(graph):
    print("=========")
    for p in graph:
        print(p)
    print("=========")
print_graph(graph)



def water(graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    spread = []
    for y in range(R):
        for x in range(C):
            if graph[y][x] == "*":
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == ".":
                        spread.append((nx, ny))
    for x, y in spread:
        graph[y][x] = "*"


def bfs(x, y):
    que = deque()
    que.append((x, y, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * C for _ in range(R)]
    visited[y][x] = True

    while que:
        x, y, time = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < C and 0 < ny < R and graph[ny][nx] == ".":
                time += 1
                que.append((nx, ny, time))


for y in range(R):
    for x in range(C):
        if graph[y][x] == "D":
            bfs(x, y)
        if graph[y][x] == "S":
            biber = [x, y]
