import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().strip().split())
jewelry = []
for n in range(N):
    # 무게 M 와 가격 V
    M, V = map(int, input().strip().split())
    heappush(jewelry, [M, V])
bags = []
for i in range(K):
    # 가방에 담을 수 있는 최대 무게 C
    C = int(input().strip())
    bags.append(C)
bags.sort()  # 가방은 작은 것부터

result = 0
price = []
for bag in bags:
    # 가방에 넣을 수 있는 무게들의 가격들만 price에 넣는다
    while jewelry and bag >= jewelry[0][0]:
        M, V = heappop(jewelry)
        heappush(price, -V)

    # 보석은 가장 큰 가치를 갖는 것을 추가
    if price:
        result += -heappop(price)
    elif not jewelry:
        break
print(result)
