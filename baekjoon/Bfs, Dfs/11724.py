import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())
dic = defaultdict(list)
visited = [False] * (N + 1)
for m in range(M):
    u, n = map(int, input().strip().split())
    dic[u].append(n)
    dic[n].append(u)


def dfs(start, cnt):
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        x = que.popleft()
        sub = dic.get(x)
        if sub is not None:
            for s in sub:
                if not visited[s]:
                    visited[s] = True
                    que.append(s)
        else:
            break
    return cnt + 1


cnt = 0
for n in range(1, N + 1):
    if not visited[n]:
        cnt = dfs(n, cnt)

print(cnt)
