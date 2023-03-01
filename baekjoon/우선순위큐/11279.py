import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
que = []

for n in range(N):
    x = int(input().strip())
    if x != 0:
        heapq.heappush(que, -1 * x)
    else:
        if len(que) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(que))
