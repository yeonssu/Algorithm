import sys
input = sys.stdin.readline


def star():
    for i in range(n):
        for j in range(n):
            if mine[i][j] == "*":
                answer[i][j] = "*"


if __name__ == "__main__":
    n = int(input().strip())
    # . : 지뢰가 없는 지점 / * : 지뢰가 있는 지점
    mine = [list(input().strip()) for _ in range(n)]
    # x : 열린 칸 / . : 열리지 않은 칸
    board = [list(input().strip()) for _ in range(n)]
    flag = False
    direction = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
    answer = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            # 지뢰가 아닌 칸이 열리면
            if board[y][x] == "x" and mine[y][x] != "*":
                cnt = 0
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and mine[ny][nx] == "*":
                        cnt += 1
                answer[y][x] = cnt
            # 지뢰가 있는 칸이 열리면, 지뢰가 있는 모든 칸이 별표(*)로 표시
            elif board[y][x] == "x" and mine[y][x] == "*":
                flag = True
            else:
                answer[y][x] = "."
    if flag:
        star()
    for ans in answer:
        for a in ans:
            print(a, end="")
        print()
