import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    board = [list(map(int, input().strip().split())) for _ in range(N)]
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().strip().split())
        x1, x2, y1, y2 = x1 - 1, x2 - 1, y1 - 1, y2 - 1
        answer = 0
        if y1 == y2:
            for i in range(x1, x2 + 1):
                answer += board[y1][i]
        else:
            for i in range(x1, N):
                answer += board[y1][i]
            for i in range(y1 + 1, y2 - y1):
                for j in range(N):
                    answer += board[i][j]
            for i in range(x2 + 1):
                answer += board[y2][i]

        print(answer)
