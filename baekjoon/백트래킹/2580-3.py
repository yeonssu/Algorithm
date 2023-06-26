from collections import deque
import sys

input = sys.stdin.readline


def vertical(x, y, num):
    # 가로
    for i in range(9):
        a = board[y][i]
        if board[y][i] == num:
            return False
    return True


def horizon(x, y, num):
    # 세로
    for i in range(9):
        b = board[i][x]
        if board[i][x] == num:
            return False
    return True


def three_to_three(x, y, num):
    # 3 x 3
    for i in range(3):
        for j in range(3):
            c = board[(y // 3) * 3 + i][(x // 3) * 3 + j]
            if board[(y // 3) * 3 + i][(x // 3) * 3 + j] == num:
                return False
    return True


def dfs(cnt):
    if cnt == len(zero):
        for b in board:
            print(*b)
        exit()

    x, y = zero[cnt]
    for num in range(1, 10):
        if vertical(x, y, num) and horizon(x, y, num) and three_to_three(x, y, num):
            board[y][x] = num
            dfs(cnt + 1)
            board[y][x] = 0


board = [list(map(int, input().strip().split())) for _ in range(9)]
zero = deque()

for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            zero.append((x, y))
dfs(0)
