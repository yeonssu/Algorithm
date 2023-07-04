import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().strip().split())
jewelry = []
for n in range(N):
    # 무게 M 와 가격 V
    M, V = map(int, input().strip().split())
    heappush(jewelry, [M, V])
print(jewelry)
bags = []
for i in range(K):
    # 가방에 담을 수 있는 최대 무게 C
    C = int(input().strip())
    bags.append(C)
bags.sort()
print(bags)  # 가방은 작은 것부터

result = 0
price = []
for bag in bags:
    while jewelry:
        M, V = heappop(jewelry)
        heappush(price, -V)  # 보석은 가장 큰 가치를 갖는 것 부터
        if price:
            result += -heappop(price)
        elif not jewelry:
            break
print(result)
