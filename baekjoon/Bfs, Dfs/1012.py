from collections import deque
import sys
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    que = deque([[a,b]])
    while que:
        index = que.popleft() 
        x = index[0]
        y = index[1]
        ground[x][y] = 0 #지나감
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N: #범위를 넘어가면
                continue
            
            if ground[nx][ny]==1:
                ground[nx][ny] = 0 #지나감
                que.append([nx,ny])


T = int(input())
for t in range(T):
    M,N,K = map(int,sys.stdin.readline().strip().split())
    ground = [[0]*N for _ in range(M)]
    for k in range(K):
        X, Y = map(int,sys.stdin.readline().strip().split())
        ground[X][Y] = 1
    
    cnt = 0
    for m in range(M):
        for n in range(N):
            if ground[m][n]==1:
                bfs(m,n)
                cnt+=1
    print(cnt)