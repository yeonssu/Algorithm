# 시간초과
import sys
input = sys.stdin.readline

# N : 필드의 수, Z : 도착해야하는 필드의 번호, M : 장애물 개수
N, Z, M = map(int, input().strip().split())
obstacle = list(map(int, input().strip().split()))

for K in range(1, N + 1):
    aram = 1
    while True:
        if aram % N == Z:
            print(K)
            exit()
        if aram % N in obstacle:
            break
        aram += K
