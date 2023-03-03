import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

que = []

for n in range(N):
    gift = list(map(int, input().strip().split()))
    if gift[0] == 0:
        if len(que) == 0:
            print(-1)
        else:
            print(-heapq.heappop(que))
    else:
        for i in range(gift[0]):
            heapq.heappush(que, -gift[i+1])
