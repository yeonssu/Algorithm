import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

# 마을(정점) N / 도로(간선) M / 파티가 열리는 마을 X
N, M, X = map(int, input().strip().split())
a_x_graph = defaultdict(list)
x_a_graph = defaultdict(list)
for _ in range(M):
    start, end, time = map(int, input().strip().split())
    a_x_graph[start].append((end, time))
    x_a_graph[end].append((start, time))


def dijkstra(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [987654321 for _ in range(N + 1)]
    distance[start] = 0

    while q:
        dist, now_node = heapq.heappop(q)

        if distance[now_node] < dist:
            continue

        for i in graph[now_node]:
            next_node = i[0]
            weight = i[1]
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance


answer = []
for i in range(1, N + 1):
    go = dijkstra(a_x_graph, i)
    back = dijkstra(X)
    answer.append(go[X] + back[i])
print(max(answer))
