import sys
from collections import deque

input = sys.stdin.readline

'''
. : 비어있는 곳 / * : 물이 차있는 지역 / X : 돌 / D : 비버의 굴 / S : 고슴도치 위치
고슴도치(S) -> 비버의 굴(D)
매 분마다 물 이동, 고슴도치 이동
'''

R, C = map(int, input().strip().split())
graph = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
water_que = deque()
dochi_que = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for y in range(R):
    for x in range(C):
        if graph[y][x] == "S":
            dochi_que.append((x, y))
            visited[y][x] = True
        elif graph[y][x] == "*":
            water_que.append((x, y))
            visited[y][x] = True
        elif graph[y][x] == "R":
            visited[y][x] = True



def dfs():
    time = 0
    while dochi_que:
        # 물 이동
        for _ in range(len(water_que)):
            x, y = water_que.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == "." and not visited[ny][nx]:
                    graph[ny][nx] = "*"
                    water_que.append((nx, ny))
                    visited[ny][nx] = True

        # 도치 이동
        for _ in range(len(dochi_que)):
            x, y = dochi_que.popleft()
            if graph[y][x] == "D":
                return time

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < C and 0 <= ny < R and (graph[ny][nx] == "." or graph[ny][nx] == "D") and not visited[ny][nx]:
                    dochi_que.append((nx, ny))
                    visited[ny][nx] = True
        time += 1
    return -1

result = dfs()
if result == -1:
    print("KAKTUS")
else:
    print(result)
