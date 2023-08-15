import sys, heapq
from collections import deque

input = sys.stdin.readline
directions = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# num, direction, x, y
fish = []
graph = [[] for _ in range(4)]
for i in range(4):
    sub = list(map(int, input().strip().split()))
    for j in range(4):
        graph[j].append((sub[2 * j], sub[2 * j + 1]))
        heapq.heappush(fish, (sub[2 * j], sub[2 * j + 1], i, j))

for p in graph:
    print(p)
# 1️⃣ 상어 (0, 0)으로 이동
# 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다.
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다.
# eat : num
# shark : x, y, dir
eat = []
eat.append(graph[0][0][0])
shark = deque()
shark.append((0, 0, directions[graph[0][0][1]]))
while shark:
    # 2️⃣ 물고기가 번호가 작은 물고기부터 순서대로 이동한다.
    # 물고기는 한 칸을 이동 가능
    # 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
    while fish:
        num, dir, y, x = heapq.heappop(fish)
        direction = directions[dir]
        print(num, direction, x, y)
        nx = x + direction[0]
        ny = y + direction[1]
        # 이동할 수 없는 칸 : 상어가 있거나, 공간의 경계를 넘는 칸
        # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
        # 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다.
        cnt = 0
        flag = True
        while nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == shark[0][0] and ny == shark[0][1]):
            if dir >= 8 or cnt >= 8:
                flag = False
                break
            dir += 1
            direction = directions[dir]
            nx = x + direction[0]
            ny = y + direction[1]
            cnt += 1

        # 이동할 수 있는 칸 : 빈 칸과 다른 물고기가 있는 칸
        if not flag:
            graph[ny][nx] = graph[y][x]
            heapq.heappush(fish, (graph[ny][nx][0], graph[ny][nx][1], x, y))
            heapq.heappush(fish, (graph[y][x][0], graph[y][x][1], nx, ny))

    # 3️⃣ 물고기의 이동이 모두 끝나면 상어 이동
    # 한 번에 여러 개의 칸을 이동할 수 있다.
    # 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
    # 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
    # 물고기가 없는 칸으로는 이동할 수 없다.
    # 상어가 이동할 수 있는 칸이 없으면 끝.
    x, y, direction = shark.popleft()
