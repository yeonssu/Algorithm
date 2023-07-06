import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 컴퓨터 수
n = int(input().strip())
t = int(input().strip())
computers = defaultdict(list)
visited = [False] * (n + 1)
for _ in range(t):
    a, b = map(int, input().strip().split())
    computers[a].append(b)
    computers[b].append(a)


def virus(start):
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        x = que.popleft()
        virus_computer = computers.get(x)
        if virus_computer is not None:
            for v in virus_computer:
                if not visited[v]:
                    visited[v] = True
                    que.append(v)
        else:
            break


virus(1)
result = 0
for i in range(2, n + 1):
    if visited[i]:
        result += 1
print(result)
