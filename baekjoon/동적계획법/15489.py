import sys
input = sys.stdin.readline


if __name__ == "__main__":
    r, c, w = map(int, input().strip().split())
    dp = [[1] * i for i in range(1, 30)]
    for i in range(2, 29):
        for j in range(1, len(dp[i]) - 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    answer = 0
    for i in range(r - 1, r + w - 1):
        for j in range(c - 1, c + i - r + 1):
            answer += dp[i][j]
    print(answer)
