import sys

N = int(sys.stdin.readline())
dot = []

for n in range(N):
    x,y = map(int,sys.stdin.readline().split())
    dot.append([x,y])

dot.sort(key=lambda x:(x[1],x[0]))

for x,y in dot:
    print(x,y)
