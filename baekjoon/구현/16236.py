import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(N)]

# 물고기 M마리, 아기 상어 1마리
# < 물고기 조건 >
# 한 칸에는 물고기 최대 1마리 존재
# 아기 상어와 물고기는 모두 크기를 가지고 있다 (자연수)
# 물고기가 먹히면, 그 칸은 빈 칸이 된다.
# < 아기 상어 조건 >
# 처음 아기 상어의 크기 : 2


# 1. 더 이상 먹을 수 있는 물고기가 공간에 없다면, 아기 상어는 엄마 상어에게 도움 요청 (종료)
# 2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리가 가까운 물고기가 많다면, 우선 순위 : 가장 위에 있는 물고기, -> 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.

start_shark = (0, 0, 2)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            start_shark = (j, i, 2)

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_eatable_fish(shark_x, shark_y, shark_size):
    visited = [[False] * N for _ in range(N)]
    visited[shark_y][shark_x] = True
    shark = deque()
    shark.append((shark_x, shark_y, 0))
    eat = []
    # 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
    while shark:
        x, y, distance = shark.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                # 아기 상어는 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다
                if graph[ny][nx] > shark_size:
                    continue
                # 아기 상어는 크기가 같은 물고기는 먹을 수 없고, 지나갈 수 있다.
                elif graph[ny][nx] == shark_size:
                    shark.append((nx, ny, distance + 1))
                    visited[ny][nx] = True
                # 아기 상어는 크기보다 작은 물고기만 먹을 수 있다.
                else:
                    shark.append((nx, ny, distance + 1))
                    visited[ny][nx] = True
                    if graph[ny][nx] != 0:
                        eat.append((nx, ny, graph[ny][nx], distance + 1))

    return sorted(eat, key=lambda x: (-x[3], -x[1], -x[0]))


answer = 0
x, y, shark_size = start_shark[0], start_shark[1], start_shark[2]
upgrade = 0
while True:
    eat = find_eatable_fish(x, y, shark_size)

    if len(eat) == 0:
        print(answer)
        exit()

    nx, ny, fish_size, distance = eat.pop()
    answer += distance
    graph[ny][nx] = 0
    graph[y][x] = 0

    x = nx
    y = ny
    upgrade += 1
    if upgrade == shark_size:
        shark_size += 1
        upgrade = 0
