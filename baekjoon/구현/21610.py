N, M = map(int, input().split())

ground = [[0] * (N + 1)]
for n in range(1, N + 1):
    sub = list()
    sub.append(0)
    for i in list(map(int, input().split())):
        sub.append(i)
    ground.append(sub)
'''
[[0, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 2], 
[0, 2, 3, 2, 1, 0], 
[0, 4, 3, 2, 9, 0], 
[0, 1, 0, 2, 9, 0], 
[0, 8, 8, 2, 1, 0]]
'''

# [[5, 1], [5, 2], [4, 1], [4, 2]]
present_clouds = [[N, 1], [N, 2], [N - 1, 1], [N - 1, 2]]

#  0, ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, 1, 0, 1, 1, 1]

for m in range(M):
    # 구름 이동
    direct, move = map(int, input().split())  # 1(방향 ←), 3(3칸)
    next_clouds = []
    for cloud in present_clouds:
        x = cloud[0]
        y = cloud[1]
        # 범위를 넘으면 연결된 곳으로
        nx = (x + dx[direct] * move) % N
        ny = (y + dy[direct] * move) % N
        if nx == 0:
            nx = N
        if ny == 0:
            ny = N
        next_clouds.append([nx, ny])
    # 이동 후 좌표 [[5, 3], [5, 4], [4, 3], [4, 4]]

    # ↖, ↗, ↘, ↙
    diagonal_dx = [-1, 1, -1, 1]
    diagonal_dy = [-1, -1, 1, 1]

    for cloud in next_clouds:
        # 구름이 있는 칸에 비가 1씩 내린다
        x = cloud[0]
        y = cloud[1]
        ground[x][y] += 1
        # print(ground[x][y])

        # 각각의 대각선 물이 있다면 증가
        cnt = 0
        for i in range(4):
            nx = x + diagonal_dx[i]
            ny = y + diagonal_dy[i]

            if 0 < nx <= N and 0 < ny <= N and ground[nx][ny] >= 1:
                cnt += 1
        ground[x][y] += cnt
        # print(ground[x][y])

    # 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2 이상인 칸에 구름이 생긴다
    # 구름이 생기면 물의 양 -2
    clouds = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if [i, j] not in next_clouds and ground[i][j] >= 2:
                ground[i][j] -= 2
                # print(i, j)
                clouds.append([i, j])
print(ground)

# 물의 양 합 계산
result = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        result += ground[i][j]
print(result)
