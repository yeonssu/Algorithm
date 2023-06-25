import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M, V = map(int, input().strip().split())
graph = defaultdict(list)
for m in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

def dfs(V):
    stack = list()
    stack.append(V)
    visited = [False] * (N + 1)

    while stack:
        start = stack.pop()
        if graph.get(start) is None or len(graph.get(start)) == 0:
            print(start, end=" ")   # 연결된 것이 없어도 그 정점 자체는 출력을 해야 합니다. https://www.acmicpc.net/board/view/119673
            break
        else:
            if not visited[start]:
                print(start, end=" ")
                stack.extend(sorted(graph.get(start), reverse=True))
                visited[start] = True


def bfs(V):
    que = deque()
    que.append(V)
    visited = [False] * (N + 1)
    visited[V] = True

    while que:
        start = que.popleft()
        print(start, end=" ")
        if graph.get(start) is None or len(graph.get(start)) == 0:
            break
        else:
            for i in sorted(list(graph.get(start))):
                if not visited[i]:
                    que.append(i)
                    visited[i] = True


dfs(V)
print()
bfs(V)
