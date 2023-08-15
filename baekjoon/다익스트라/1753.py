import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

# 정점 V / 간선 E
V, E = map(int, input().strip().split())

# 시작 정점 번호 K
K = int(input().strip())
graph = defaultdict(list)

# u에서 v로 가는 가중치 w
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))

answer = [987654321 for _ in range(V + 1)]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    answer[start] = 0

    while q:
        dist, now_node = heapq.heappop(q)

        if answer[now_node] < dist:
            continue

        for i in graph[now_node]:
            next_node = i[0]
            weight = i[1]

            cost = dist + weight
            if cost < answer[next_node]:
                answer[next_node] = cost
                heapq.heappush(q, (cost, next_node))


dijkstra(K)

for i in range(1, V + 1):
    if answer[i] == 987654321:
        print("INF")
    else:
        print(answer[i])
