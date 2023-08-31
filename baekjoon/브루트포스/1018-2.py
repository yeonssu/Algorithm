import sys
input = sys.stdin.readline


def count_diff(n, m, start):
    cnt = 0
    for i in range(n, n + 8):
        for j in range(m, m + 8):
            if (i - n) % 2 == 0:
                if (j - m) % 2 == 0 and start != board[i][j]:
                    cnt += 1
                elif (j - m) % 2 == 1 and start == board[i][j]:
                    cnt += 1
            elif (i - n) % 2 == 1:
                if (j - m) % 2 == 0 and start == board[i][j]:
                    cnt += 1
                elif (j - m) % 2 == 1 and start != board[i][j]:
                    cnt += 1
    return cnt


N, M = map(int, input().strip().split())
board = [list(map(str, input().strip())) for _ in range(N)]
answer = 987654321
for n in range(N - 7):
    for m in range(M - 7):
        for start in ["B", "W"]:
            cnt = count_diff(n, m, start)
            answer = min(answer, cnt)
print(answer)
