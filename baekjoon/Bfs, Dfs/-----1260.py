from collections import deque,defaultdict
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

node, edge, start = map(int,input().split())
graph = defaultdict(list)
for i in range(edge):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

print(graph)

print(*dfs(graph,start))
print(*bfs(graph,start))