import sys, math
from collections import defaultdict
from heapq import heappush, heappop


input = sys.stdin.readline

T = int(input().strip())


# def dijkstra(graph, start):
#     distances = defaultdict(float)
#     # start 로 부터의 거리 값 저장
#     for node in graph:
#         distances[node] = float('inf')
#     distances[start] = 0  # 시작 값은 0이어야 함
#     queue = []
#     heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.
#
#     while queue:  # queue에 남아 있는 노드가 없으면 끝
#         current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
#
#         if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
#             continue
#
#         for value in graph.get(current_destination):
#             new_destination, new_distance = value[0], value[1]
#             distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
#             if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
#                 distances[new_destination] = distance
#                 heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
#
#     return distances

def dijkstra(graph, times, start):
    heappush(heap, [start, 0])
    times[start] = 0
    while heap:
        current_node, current_time = heappop(heap)
        for next_node, next_time in graph[current_node]:
            # 더 작은 값으로 갱신
            if next_time + current_time < times[next_node]:
                times[next_node] = next_time + current_time
                heappush(heap, [next_node, next_time + current_time])
    return times


for t in range(T):
    # n : 컴퓨터 개수 / d : 의존성 개수 / c : 해킹 당한 컴퓨터 번호
    n, d, c = map(int, input().strip().split())
    graph = defaultdict(list)
    heap = []
    times = [math.inf] * (n + 1)
    for _ in range(d):
        # 컴퓨터 a가 컴퓨터 b를 의존
        # 컴퓨터 b가 감염 -> s초 후 컴퓨터 a도 감염됨
        a, b, s = map(int, input().strip().split())
        graph[b].append((a, s))

    times = dijkstra(graph, times, c)
    cnt = 0
    ans = 0
    for i in times:
        if i != math.inf:
            cnt += 1
            ans = max(ans, i)
    print(cnt, end=" ")
    print(ans)
