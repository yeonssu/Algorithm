import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().strip().split())

coins = []
for n in range(N):
    coin = int(input().strip())
    if coin <= K:
        coins.append(coin)

coins.reverse()

result = K
cnt = 0
for coin in coins:
    while result > 0:
        result -= coin
        cnt += 1
    if result < 0:
        result += coin
        cnt -= 1
print(cnt)
