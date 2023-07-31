import sys

input = sys.stdin.readline


def sand_count(x, y, spread):
    global answer

    not_a = 0
    for dx, dy, z in spread:
        nx = x + dx
        ny = y + dy
        if z == 'a':
            new_sand = graph[x][y] - not_a
        else:
            new_sand = int(graph[x][y] * z)
            not_a += new_sand

        if 0 <= nx < N and 0 <= ny < N:
            graph[nx][ny] += new_sand
        else:
            answer += new_sand


N = int(input().strip())

# r : y / c : x
graph = [list(map(int, input().strip().split())) for _ in range(N)]
# x, y, z
left = [(0, -2, 0.02),
        (-1, -1, 0.1), (0, -1, 0.07), (1, -1, 0.01),
        (-2, 0, 0.05), (-1, 0, 'a'),
        (-1, 1, 0.1), (0, 1, 0.07), (1, 1, 0.01),
        (0, 2, 0.02)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

start_x, start_y = N // 2, N // 2
answer = 0
time = 0
direction = {0: left, 1: down, 2: right, 3: up}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(2 * N - 1):
    d = i % 4
    if d == 0 or d == 2:
        time += 1

    for _ in range(time):
        now_x = start_x + dx[d]
        now_y = start_y + dy[d]
        sand_count(now_x, now_y, direction.get(d))
        start_x = now_x
        start_y = now_y

print(answer)
