import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

board = []
for n in range(N):
    board.append(input().strip())

vertical = 0
for n in range(N):
    vertical_line = board[n]
    if "X" not in vertical_line:
        vertical += 1

horizontal = 0
for m in range(M):
    horizontal_line = []
    for n in range(N):
        horizontal_line.append(board[n][m])
    if "X" not in horizontal_line:
        horizontal += 1

print(max(vertical, horizontal))
