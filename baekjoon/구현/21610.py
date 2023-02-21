import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

ground = [[0] * (N + 1)]
for n in range(1, N + 1):
    sub = [0]
    for i in list(map(int, input().strip().split())):
        sub.append(i)
    ground.append(sub)

present_clouds = [(N, 1), (N, 2), (N - 1, 1), (N - 1, 2)]

#  0, ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = (0, -1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 0, -1, -1, -1, 0, 1, 1, 1)

for m in range(M):
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    # 구름 이동
    direct, move = map(int, input().strip().split())
    next_clouds = []
    for x, y in present_clouds:
        # 범위를 넘으면 연결된 곳으로
        nx = (x + dx[direct] * move) % N
        ny = (y + dy[direct] * move) % N
        if nx == 0:
            nx = N
        if ny == 0:
            ny = N
        next_clouds.append((nx, ny))
        # 새로운 구름 위치 True 설정
        visited[nx][ny] = True
        # 구름이 이동한 후 비가 1씩 내린다
        ground[nx][ny] += 1

    # ↖, ↗, ↘, ↙
    diagonal_dx = (-1, 1, -1, 1)
    diagonal_dy = (-1, -1, 1, 1)

    # 각각의 대각선 물이 있다면 증가
    for x, y in next_clouds:
        cnt = 0
        for i in range(4):
            nx = x + diagonal_dx[i]
            ny = y + diagonal_dy[i]

            if 0 < nx <= N and 0 < ny <= N and ground[nx][ny] >= 1:
                cnt += 1
        ground[x][y] += cnt

    # 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2 이상인 칸에 구름이 생긴다
    # 구름이 생기면 물의 양 -2
    present_clouds = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not visited[i][j] and ground[i][j] >= 2:
                ground[i][j] -= 2
                present_clouds.append((i, j))

# 물의 양 합 계산
result = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        result += ground[i][j]
print(result)
