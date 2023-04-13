import sys


def count_candy(N, board):
    max_cnt = 0
    for i in range(N):
        # 아래랑 비교하기
        cnt = 1
        for j in range(N - 1):
            if board[j][i] == board[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        # 오른쪽이랑 비교하기
        cnt = 1
        for j in range(N - 1):
            if board[i][j] == board[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt


input = sys.stdin.readline
N = int(input().strip())
board = [list(input().strip()) for n in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        # 오른쪽이랑 바꾸기
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            answer = max(count_candy(N, board), answer)
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

        # 아래랑 바꾸기
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(count_candy(N, board), answer)
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

print(answer)
