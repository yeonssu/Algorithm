import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    dp = [[0] * 21 for _ in range(n - 1)]
    dp[0][nums[0]] = 1

    for i in range(1, n - 1):
        for j in range(21):
            if j - nums[i] >= 0:
                dp[i][j] += dp[i - 1][j - nums[i]]
            if j + nums[i] <= 20:
                dp[i][j] += dp[i - 1][j + nums[i]]

    print(dp[n - 2][nums[-1]])
