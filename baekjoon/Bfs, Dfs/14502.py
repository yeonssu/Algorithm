import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = []
for n in range(N):
    graph.append(list(map(int, input().strip().split())))


# 0 : 빈 칸 / 1 : 벽 / 2 : 바이러스가 있는 곳
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

def bfs(graph, answer):
    que = deque()
    sub_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                que.append((j, i))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and sub_graph[ny][nx] == 0:
                sub_graph[ny][nx] = 2
                que.append((nx, ny))
    cnt = count_zero(sub_graph)
    answer = max(cnt, answer)
    return answer


def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


wall = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            wall.append((j, i))

answer = 0
for combi in combinations(wall, 3):
    a, b, c = combi[0], combi[1], combi[2]
    graph[a[1]][a[0]] = 1
    graph[b[1]][b[0]] = 1
    graph[c[1]][c[0]] = 1
    answer = bfs(graph, answer)
    graph[a[1]][a[0]] = 0
    graph[b[1]][b[0]] = 0
    graph[c[1]][c[0]] = 0
print(answer)
