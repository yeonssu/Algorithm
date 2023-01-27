from collections import deque
import sys
M, N = map(int,sys.stdin.readline().strip().split())

box = []
que = deque([])
#익은토마토 저장
for n in range(N):
    box.append(list(map(int,sys.stdin.readline().strip().split())))
    for m in range(M):
        if box[n][m] == 1:
            que.append([n,m])

dx = [1,-1,0,-0]
dy = [0,0,1,-1]
def bfs():
    while que:
        val = que.popleft() 
        x = val[0]
        y = val[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: #범위를 넘어가면
                continue
            if box[nx][ny]==0:
                box[nx][ny] = box[x][y] + 1
                que.append([nx,ny])

bfs()
cnt = 0
for i in box:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt-1)