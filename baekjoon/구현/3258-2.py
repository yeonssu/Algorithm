import sys
input = sys.stdin.readline

# N : 필드의 수, Z : 도착해야하는 필드의 번호, M : 장애물 개수
N, Z, M = map(int, input().strip().split())
obstacle = list(map(int, input().strip().split()))

for K in range(1, N):
    aram_location = [(1 + K * n) % N for n in range(N)]
    for aram in aram_location:
        if aram == 0:
            aram = N
        if aram in obstacle:
            break
        if aram == Z:
            print(K)
            exit()
