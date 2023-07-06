import copy
import sys
input = sys.stdin.readline


# def cctv(graph, start_x, start_y, num):
#     if num == 1:
#
#     elif num == 2:
#
#     elif num == 3:
#
#     elif num == 4:
#
#     elif num == 5:
#         for x in range(0, start_x):
#             if graph[start_y][x] == 0:
#                 graph[start_y][x] = "#"
#             elif graph[start_y][x] == 6:
#                 break
#             else:
#                 continue
#         for x in range(start_x + 1, M):
#             if graph[start_y][x] == 0:
#                 graph[start_y][x] = "#"
#             elif graph[start_y][x] == 6:
#                 break
#             else:
#                 continue
#         for y in range(0, start_y):
#             if graph[y][start_x] == 0:
#                 graph[y][start_x] = "#"
#             elif graph[y][start_x] == 6:
#                 break
#             else:
#                 continue
#         for y in range(start_y, M):
#             if graph[y][start_x] == 0:
#                 graph[y][start_x] = "#"
#             elif graph[y][start_x] == 6:
#                 break
#             else:
#                 continue
#
#     return graph


def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


N, M = map(int, input().strip().split())

mode = {1: [[0], [1], [2], [3]], 2: ["좌우", "상하"], 3: ["좌상", "좌하", "우상", "우하"],
        4: ["하좌우", "상좌우", "상하우", "상하좌"], 5: ["상하좌우"]}

direction = [(-1, 0), ()]

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

sub_graph = copy.deepcopy(graph)
