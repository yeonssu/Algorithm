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
    if result >= 0:
        tem_cnt = result // coin
        result -= coin * tem_cnt
        cnt += tem_cnt
    else:
        break
print(cnt)
