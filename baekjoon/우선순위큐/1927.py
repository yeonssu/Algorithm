import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input().strip())
que = PriorityQueue()

for n in range(N):
    x = int(input().strip())
    if x != 0:
        que.put(x)
    else:
        if que.qsize() == 0:
            print(0)
        else:
            print(que.get())
