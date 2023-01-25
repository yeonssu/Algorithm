from collections import deque
def bfs(graph,start):
    visited = [start]
    que = deque([start])
    while que:
        v = que.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                que.append(i)
    return visited
    
N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))
print(bfs(graph,0))

print(graph)
