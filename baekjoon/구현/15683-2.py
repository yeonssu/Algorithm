import copy
import sys

input = sys.stdin.readline


def watch(x, y, direction, graph):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += direction_list[d][0]
            ny += direction_list[d][1]
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이면 종료
                if graph[nx][ny] == 6:
                    break
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
                else:
                    continue
            # 벗어나면 종료
            else:
                break


def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


N, M = map(int, input().strip().split())

# 1 : 상, 하, 좌, 우 / 2 : 상하, 좌우 / 3 : 상좌, 상우, 하좌, 하우 /
# 4 : 상하좌, 상하우, 상좌우, 하좌우 / 5 : 상하좌우
mode = {1: [[0], [1], [2], [3]], 2: [[0, 1], [2, 3]], 3: [[0, 2], [0, 3], [1, 2], [1, 3]],
        4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], 5: [[0, 1, 2, 3]]}

# 상 하 좌 우
direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

graph = []
# 0 : 빈 칸 / 6 : 벽 / 1~5 : CCTV
for n in range(N):
    graph.append(list(map(int, input().strip().split())))

cctv_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 or graph[i][j] == 6:
            continue
        else:
            cctv_list.append((i, j, graph[i][j]))

depth = len(cctv_list)
sub_graph = copy.deepcopy(graph)

count = 0
answer = 0
while True:
    x, y, cctv_type = cctv_list[count]
    for cctv_dir in mode.get(cctv_type):
        watch(x, y, cctv_dir, sub_graph)
        answer = count_zero(graph)
    count += 1
    if count == depth:
        print(answer)
        break
