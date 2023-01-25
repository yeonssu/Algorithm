from collections import deque
def dfs(graph,start):
    stack = [start]
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(reversed(graph[v]))
    return visited

def bfs(graph,start):
    que = deque([start])
    visited = [start]
    while que:
        v = que.popleft()
        for i in graph[v]:
            if i not in visited:
                que.append(i)
                visited.append(i)
    return visited