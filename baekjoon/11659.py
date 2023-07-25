import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
number = list(map(int, input().strip().split()))
prefix_sum = [0] * (N + 1)
for n in range(N):
    prefix_sum[n + 1] = prefix_sum[n] + number[n]
print(prefix_sum)
for m in range(M):
    i, j = map(int, input().strip().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
