# 5, 6을 모아서 하려했는데 이 방법으로는 안되는 것 같다...

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

no_repeat = [[False for _ in range(19)] for _ in range(19)]
win = []
answer = []
for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            for k in range(4):
                cnt = 1
                nx = x + dx[k]
                ny = y + dy[k]
                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y] and not no_repeat[nx][ny]:
                    cnt += 1

                    if cnt == 5:
                        win.append((board[x][y], cnt))
                        answer.append((x + 1, y + 1))
                    if cnt == 6:
                        win.append((board[x][y], cnt))
                        answer.append((x + 1, y + 1))
                        print(x + dx[k])
                        print(y + dy[k])
                        no_repeat[x + dx[k]][y + dy[k]] = True
                        break

                    nx = nx + dx[k]
                    ny = ny + dy[k]
print(win)
print(answer)

if len(answer) == 1:
    print(win[0][0])
    print(*answer[0])
else:
    if len(answer) != len(set(answer)):
        winner = []
        location = []
        for i in range(len(win)):
            if i == len(win) - 1 and win[i][1] != 6:
                winner.append(win[i][0])
                location.append(answer[i])
            if i + 1 < len(win) and win[i] == win[i + 1]:
                winner.append(win[i][0])
                location.append(answer[i])
        print(winner)
        print(location)
    else:
        print(0)
