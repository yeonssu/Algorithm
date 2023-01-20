import sys
N, M = map(int,sys.stdin.readline().split())

#N, M = map(int,input().split())
listen = []
see = []

for n in range(N):
    listen.append(sys.stdin.readline())

for m in range(M):
    see.append(sys.stdin.readline())
nolistennosee = list(set(listen)&set(see))
nolistennosee.sort()

print(len(nolistennosee))
for i in nolistennosee:
    print(i)