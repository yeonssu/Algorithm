import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    board = [list(map(int, input().strip().split())) for _ in range(N)]
    cumulative = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cumulative[i][j] = cumulative[i][j - 1] + cumulative[i - 1][j] - cumulative[i - 1][j - 1] + board[i - 1][j - 1]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().strip().split())
        answer = cumulative[x2][y2] - cumulative[x2][y1 - 1] - cumulative[x1 - 1][y2] + cumulative[x1 - 1][y1 - 1]
        print(answer)
