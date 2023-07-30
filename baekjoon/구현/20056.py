import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().strip().split())
graph = [[deque() for _ in range(N)] for _ in range(N)]
fireballs = deque()
# 파이어볼 위치 : (r, c) / 질량 : m / 방향 : d / 속력 : s
# 행 : y = r / 열 : x = c
for _ in range(M):
    r, c, m, s, d = map(int, input().strip().split())
    fireballs.append((r - 1, c - 1))
    graph[r - 1][c - 1].append((m, s, d))

move = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

# 1. 파이어볼 이동 -> 2. 같은 칸에 있는 파이어볼 하나로 합쳐짐 -> 파이어볼 4개로 분리
# 질량 : (합쳐진 파이어볼 질량의 합)/5
# 속력 : (합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)
# 방향 : 합쳐지는 파이어볼의 방향이 모두 홀수, 모두 짝수이면 -> 0, 2, 4, 6 / 그렇지 않으면 1, 3, 5, 7

for k in range(K):
    # 1. 파이어볼 이동
    while fireballs:
        r, c = fireballs.popleft()
        m, s, d = graph[r][c].popleft()
        nr = (r + move[d][1] * s) % N
        nc = (c + move[d][0] * s) % N
        graph[nr][nc].append((m, s, d))

    # 2. 2개 이상의 파이어볼이 있는 칸에서는 파이어볼 4개로 분리
    for r in range(N):
        for c in range(N):
            if len(graph[r][c]) >= 2:
                # 질량 : (합쳐진 파이어볼 질량의 합)/5
                # 속력 : (합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)
                # 방향 : 합쳐지는 파이어볼의 방향이 모두 홀수, 모두 짝수이면 -> 0, 2, 4, 6
                total_mass, total_speed, count_even = 0, 0, 0
                length = len(graph[r][c])
                while graph[r][c]:
                    m, s, d = graph[r][c].popleft()
                    total_mass += m
                    total_speed += s
                    # 짝수면 증가
                    if d % 2 == 0:
                        count_even += 1

                if count_even == length or count_even == 0:
                    directions = (0, 2, 4, 6)
                else:
                    directions = (1, 3, 5, 7)

                if total_mass // 5 == 0:
                    continue

                for direction in directions:
                    graph[r][c].append((total_mass // 5, total_speed // length, direction))
                    fireballs.append((r, c))
            elif len(graph[r][c]) == 1:
                fireballs.append((r, c))

answer = 0
for y in range(N):
    for x in range(N):
        if len(graph[y][x]) >= 1:
            for m, s, d in graph[y][x]:
                answer += m
print(answer)
