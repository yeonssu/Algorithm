import sys
from itertools import combinations
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input().strip())
population = defaultdict(int)
i = 1
for p in list(map(int, input().strip().split())):
    population[i] = p
    i += 1
print()
print(population)

'''
link = [[0] * (N + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    sub = list(map(int, input().strip().split()))
    M = sub[0]
    for m in range(1, M + 1):
        link[n][sub[m]] = 1
for g in link[1:]:
    print(*g[1:])
print()
'''

link = defaultdict(list)
for n in range(1, N + 1):
    sub = list(map(int, input().strip().split()))
    M = sub[0]
    for m in range(1, M + 1):
        link[n].append(sub[m])


def bfs(zone):
    start = zone[0]
    que = deque([start])
    visited = {start}
    sum = 0
    while que:
        v = que.popleft()
        sum += population[v]
        for i in link[v]:
            if i not in visited and i in zone:
                que.append(i)
                visited.add(i)
    return sum, len(visited)


result = 987654321
for i in range(1, N // 2 + 1):
    combis = list(combinations(range(1, N + 1), i))
    for combi in combis:
        zone_a = list(combi)
        zone_b = [i for i in range(1, N + 1) if i not in zone_a]
        print(zone_a)
        print(zone_b)
        sum_a, visit_a = bfs(zone_a)
        sum_b, visit_b = bfs(zone_b)
        if visit_a + visit_b == N:
            result = min(result, abs(sum_a - sum_b))

if result == 987654321:
    print(-1)
else:
    print(result)
