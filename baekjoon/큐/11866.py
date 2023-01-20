from collections import deque

N, K = map(int,input().split())

numlist = deque(list(range(1,N+1)))
result=[]
a=1

while numlist:
    n = numlist.popleft() #빼고

    if a%K==0: #3주기마다 출력
        result.append(n)
    else: #나머지는 다시 넣기
        numlist.append(n)
    a+=1
    
print("<",end="")
for i in range(len(result)-1):
    print(result[i],end=", ")
print(str(result.pop())+">")

