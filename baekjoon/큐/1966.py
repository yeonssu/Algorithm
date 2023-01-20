from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    que = deque(importance)

    cnt=0
    while que:
        maxvalue = max(que)
        a = que.popleft()
        
        if a<maxvalue: 
            que.append(a)
        else:
            cnt+=1
            if M==0:
                print(cnt)
                break

        M -= 1
        if M<0:
            M = len(que)-1
        