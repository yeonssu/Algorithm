import sys

input = sys.stdin.readline

N, M, H = map(int, input().strip().split())
graph = [[0] * (N + 1) for _ in range(H + 1)]

# b번 세로 선과 b+1번 세로 선을 a번 점선 위치에서 연결함
for m in range(M):
    a, b = map(int, input().strip().split())
    graph[a][b] = 1

for p in graph:
    print(p)


def is_i(graph):
    for start in range(1, N + 1):
        x = start
        for y in range(1, H + 1):
            if graph[y][x] == 1:
                x += 1
            elif x - 1 > 0 and graph[y][x - 1] == 1:
                x -= 1

        if x != start:
            return False

    return True


def game_start(cnt, x, y):
    global answer
    if is_i(graph):
        answer = cnt
        return
    elif answer <= cnt:
        return
    elif cnt == 3:
        return

    for i in range(y, H + 1):
        if i == y:
            k = x
        else:
            k = 0
        for j in range(k, N + 1):
            if graph[i][j] == 0:
                graph[i][j] = 1
                game_start(cnt + 1, x, y + 2)
                graph[i][j] = 0


answer = 4
game_start(0, 0, 0)
if answer < 4:
    print(answer)
else:
    print(-1)
