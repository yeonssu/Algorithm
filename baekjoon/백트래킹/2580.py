import collections
import sys

input = sys.stdin.readline

board = [list(map(int, input().strip().split())) for _ in range(9)]
zero = collections.deque()

for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            zero.append((x, y))


def vertical(x, y, num):
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


while zero:
    x, y = zero.popleft()
    for num in range(1, 10):
        if vertical(x, y, num):
            if horizon(x, y, num):
                if three_to_three(x, y, num):
                    board[y][x] = num
                    break

for p in board:
    print(*p)
