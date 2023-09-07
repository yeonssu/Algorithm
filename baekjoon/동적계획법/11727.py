import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    dp = [1, 3]
    for i in range(2, n + 1):
        dp.append((dp[i - 1] % 10007 + 2 * dp[i - 2] % 10007) % 10007)
    print(dp[n - 1] % 10007)
