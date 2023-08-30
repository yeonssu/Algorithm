import sys
from collections import deque

input = sys.stdin.readline

N, M, fuel = map(int, input().strip().split())
start_fuel = fuel
graph = [list(map(int, input().strip().split())) for _ in range(N)]
taxi_start_y, taxi_start_x = map(int, input().strip().split())
taxi_start_x -= 1
taxi_start_y -= 1
# 백준이 태울 승객을 고를 때
# 거리가 가장 짧은 승객 > 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객 > 그중 열 번호가 가장 작은 승객
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check_distance(x, y):
    visited = [[-1] * N for _ in range(N)]
    visited[y][x] = 0
    taxi = deque()
    taxi.append((x, y))
    passenger = []
    while taxi:
        x, y = taxi.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] != -1:
                if graph[ny][nx] != 1:
                    taxi.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1
                    if graph[ny][nx] == 5:
                        passenger.append((nx, ny))
    return sorted(passenger, key=lambda x: (-x[2], -x[1], -x[0]))


end = [[(0, 0)] * N for _ in range(N)]
# x : 열 / y : 행
for _ in range(M):
    start_y, start_x, end_y, end_x = map(int, input().strip().split())
    start_x -= 1
    start_y -= 1
    end_x -= 1
    end_y -= 1
    graph[start_y][start_x] = 5
    end[start_y][start_x] = (end_x, end_y)

cnt = 0
while fuel >= 0:
    passenger = check_distance(taxi_start_x, taxi_start_y)
    print(passenger)
    # 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력
    if len(passenger) == 0:
        # 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.
        if cnt == 0:
            print(-1)
        else:
            print(fuel)
        exit()
    p_x, p_y, p_distance = passenger.pop()
    fuel -= p_distance
    # 모든 손님을 이동시킬 수 없는 경우 -1 출력
    if fuel < 0:
        print(-1)
        exit()
    p_end_x, p_end_y = end[p_y][p_x]
    move_distance = abs(p_x - p_end_x) + abs(p_y - p_end_y)
    fuel -= move_distance
    if fuel < 0:
        print(-1)
        exit()
    fuel += move_distance * 2
    taxi_start_x, taxi_start_y = p_end_x, p_end_y
    cnt += 1
    graph[p_y][p_x] = 0
