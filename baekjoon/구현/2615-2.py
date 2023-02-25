import sys

input = sys.stdin.readline

board = []
for _ in range(19):
    board.append(list((map(int, input().strip().split()))))

# 1이 검은 돌, 2가 흰 돌
# 검은색이 이기면 1, 흰색이 이기면 2, 승부가 결정되지 않았으면 0을 출력
# ↓, ↘, →, ↗ 네 방향만 보면 된다
dx = (1, 1, 0, -1)
dy = (0, 1, 1, 1)

win = []
answer = []
for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            for k in range(4):
                cnt = 1
                nx = x + dx[k]
                ny = y + dy[k]
                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y]:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and board[x - dx[k]][y - dy[k]] == board[x][y]:
                            break
                        if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and board[nx + dx[k]][ny + dy[k]] == board[x][
                            y]:
                            break
                        print(board[x][y])
                        print(x + 1, y + 1)
                        sys.exit()
                    nx += dx[k]
                    ny += dy[k]

print(0)
