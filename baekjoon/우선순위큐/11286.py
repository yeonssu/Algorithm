import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
que = []
origin = dict()

for n in range(N):
    x = int(input().strip())
    if x != 0:
        heapq.heappush(que, (abs(x), x))
    else:
        if len(que) == 0:
            print(0)
        else:
            print(heapq.heappop(que)[1])
