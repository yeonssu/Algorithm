# solution 1
from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def bfs(graph,start):
    queue = deque([start])
    visited = [start]
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                    queue.append(i)
                    cnt+=1
                    visited.append(i)
    return cnt

T = int(input())
for i in range(T):
    graph = defaultdict(list)

    Node, Edge = map(int,input().split())
    for j in range(Edge):
        n1, n2 = map(int,input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for k in graph:
        graph[k] = list(set(graph[k]))

    print(bfs(graph,1))


# solution 2
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    for _ in range(M):
        u, v = map(int, input().split())
    print(N-1)