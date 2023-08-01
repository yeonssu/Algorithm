def sand_count(x, y, direction):
    global answer

    not_a = 0
    for dx, dy, z in direction:
        nx = x + dx
        ny = y + dy
        if z == 0:
            new_sand = sand[x][y] - not_a
        else:
            new_sand = int(sand[x][y] * z)
            not_a += new_sand

        if 0 <= nx < N and 0 <= ny < N:
            sand[nx][ny] += new_sand
        else:
            answer += new_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

start_x, start_y = N // 2, N // 2
answer = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

directions = {0: left, 1: down, 2: right, 3: up}
time = 0
for i in range(2 * N - 1):
    d = i % 4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        now_x = start_x + dx[d]
        now_y = start_y + dy[d]
        if 0 <= now_x < N and 0 <= now_y < N:
            sand_count(now_x, now_y, directions[d])
        start_x, start_y = now_x, now_y

print(answer)
