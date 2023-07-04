import sys, math
from collections import defaultdict

input = sys.stdin.readline

T = int(input().strip())


# 가장 최소 거리를 가지는 정점 반환
def get_small_index():
    min_value = math.inf
    index = 0
    for i in range(n):
        if answer[i] < min_value and not visited[i]:
            min_value = answer[i]
            index = i
    return index


def dijkstra(start):
    for i in range(n):
        answer[i] = graph[start][i]
    visited[start] = True
    for i in range(n - 2):
        small_index = get_small_index()
        visited[small_index] = True
        for j in range(n):
            if not visited[j] and answer[small_index] + graph[small_index][j] < answer[j]:
                answer[j] = answer[small_index] + graph[small_index][j]


for t in range(T):
    # n : 컴퓨터 개수 / d : 의존성 개수 / c : 해킹 당한 컴퓨터 번호
    n, d, c = map(int, input().strip().split())
    graph = [[math.inf] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    answer = [0] * (n + 1)
    for _ in range(d):
        # 컴퓨터 a가 컴퓨터 b를 의존
        # 컴퓨터 b가 감염 -> s초 후 컴퓨터 a도 감염됨
        a, b, s = map(int, input().strip().split())
        graph[a][b] = s
    for p in graph:
        print(p)
    print("-----------")
    dijkstra(c)
    print(answer)
    print("================")
