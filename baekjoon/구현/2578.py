import sys
input = sys.stdin.readline


def bingo():
    cnt = 0
    # 가로
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                break
            if j == 4 and board[i][j] == -1:
                cnt += 1
    # 세로
    for j in range(5):
        for i in range(5):
            if board[i][j] != -1:
                break
            if i == 4 and board[i][j] == -1:
                cnt += 1
    # 대각선
    for k in range(5):
        if board[k][k] != -1:
            break
        if k == 4 and board[k][k] == -1:
            cnt += 1
    # 대각선
    for k in range(5):
        if board[k][4 - k] != -1:
            break
        if k == 4 and board[k][4 - k] == -1:
            cnt += 1
    return cnt


def check(idx, value):
    for i in range(5):
        for j in range(5):
            if board[i][j] == value:
                board[i][j] = -1
                answer = bingo()
                if answer >= 3:
                    print(idx + 1)
                    exit()
                return


if __name__ == "__main__":
    board = [list(map(int, input().strip().split())) for _ in range(5)]
    moderator = []
    for _ in range(5):
        moderator.extend(list(map(int, input().strip().split())))
    for idx, value in enumerate(moderator):
        check(idx, value)
