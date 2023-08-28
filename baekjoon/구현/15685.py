import sys
input = sys.stdin.readline

# K(K > 1)세대 드래곤 커브 : K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 -> 그것을 끝 점에 붙인다
# 끝 점 : 시작 점에서 선분을 타고 이동했을 때, 가장 먼 거리에 있는 점
N = int(input().strip())
# 방향 (0 : → / 1 : ↑ / 2 : ← / 3 : ↓)
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
graph = [[0] * 101 for _ in range(101)]
for _ in range(N):
    # x : 드래곤 커브의 시작 점 / y : 드래곤 커브의 시작 점 / d : 시작 방향 / g : 세대
    x, y, d, g = map(int, input().strip().split())
    graph[y][x] = 1

    curve = [d]
    for _ in range(g):
        for d in reversed(range(len(curve))):
            curve.append((curve[d] + 1) % 4)

    for d in curve:
        x += directions[d][0]
        y += directions[d][1]
        if 0 <= x < 101 and 0 <= y < 101:
            graph[y][x] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1
print(answer)

