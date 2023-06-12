import sys

input = sys.stdin.readline
# 세로 R, 가로 C
R, C, T = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for r in range(R)]


# 미세먼지 확산
def diffuse():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 더할 것들은 따로 모아서 마지막에 한 번에 더해준다(그 때 그 때 더하면 안 됨)
    plus = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            # 공기청정기가 없고, 미세먼지가 있는 곳은 확산
            if board[y][x] != -1 and board[y][x] != 0:
                # 상 하 좌 우, 뺄 것들을 모아서 한 번에 뺀다
                minus = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 인접한 방향에 공기청정기가 없고 칸이 있으면 확산이 일어난다
                    if 0 <= nx < C and 0 <= ny < R and board[ny][nx] != -1:
                        plus[ny][nx] += board[y][x] // 5
                        minus += board[y][x] // 5
                board[y][x] -= minus

    for y in range(R):
        for x in range(C):
            board[y][x] += plus[y][x]


def clean_up(up):
    # 아래 -> 오른쪽 -> 위 -> 왼쪽
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    x, y = 1, up
    k = 0
    before = 0
    while True:
        nx = x + dx[k]
        ny = y + dy[k]
        if x == 0 and y == up:
            break
        if nx < 0 or nx >= C or ny < 0 or ny >= R:
            k += 1
            continue
        board[y][x], before = before, board[y][x]
        x = nx
        y = ny


def clean_down(down):
    # 위 -> 오른쪽 -> 아래 -> 왼쪽
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x, y = 1, down
    k = 0
    before = 0
    while True:
        nx = x + dx[k]
        ny = y + dy[k]
        if x == 0 and y == down:
            break
        if nx < 0 or nx >= C or ny < 0 or ny >= R:
            k += 1
            continue
        board[y][x], before = before, board[y][x]
        x = nx
        y = ny


up = 0
down = 0
for y in range(R):
    if board[y][0] == -1:
        up = y
        down = y + 1
        break

for t in range(T):
    diffuse()
    clean_up(up)
    clean_down(down)

# 정답
result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            result += board[i][j]
print(result)
