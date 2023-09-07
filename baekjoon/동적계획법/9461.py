import sys
input = sys.stdin.readline
if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        dp = [1, 1, 1]
        for i in range(3, N):
            dp.append(dp[i - 2] + dp[i - 3])
        print(dp[N - 1])