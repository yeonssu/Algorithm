import sys
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        n, m = map(int, input().strip().split())
        if n == 0 and m == 0:
            break
        graph = [list(map(int, input().strip().split())) for _ in range(n)]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        answer = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if graph[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i -  1][j - 1]) + 1
                    answer = max(answer, dp[i][j])
        print(answer)

