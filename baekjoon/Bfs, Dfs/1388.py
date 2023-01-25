from collections import deque
import sys

def bfs(a,b):
    que = deque([[a,b]]) #[0,0]
    while que:
        index = que.popleft() 
        x = index[0] #index[0]=0
        y = index[1] #index[1]=0
        if graph[x][y]=="-": #graph의 값이 -면 
            graph[x][y] = 1 #지나감
            # 다음값이 범위를 안넘을 때
            if  y+1 < M:
                if graph[x][y+1]!="-": # 바로 오른쪽이 -가 아니면 끝
                    break
                else:                  # 바로 오른쪽이 -가 맞으면 큐에 넣고 그 오른쪽 검사
                    que.append([x,y+1])
        elif graph[x][y]=="|": #graph의 값이 |면
            graph[x][y] = 1
            # 아래값이 범위를 안넘을 때
            if x+1 < N:
                if graph[x+1][y]!="|": # 바로 아래가 |이 아니면 끝
                    break
                else:                   #바로 아래가 |이면 큐에 넣고 그 아래 검사
                    que.append([x+1,y])


#가로 M, 세로 N
N, M = map(int,input().split())
graph = [list(sys.stdin.readline().strip()) for n in range(N)]

cnt = 0
for n in range(N):
    for m in range(M):
        if graph[n][m] != 1 :
            bfs(n,m)
            cnt+=1

print(cnt)

#근데 왜 cnt+1를 37번째 줄에 안쓰고 break전에 쓰면 실행이 안될까?