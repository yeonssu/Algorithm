# sol 1
N = int(input())

def hansu(N):
    cnt = 0
    for i in range(1,N+1):
        lst = list(map(int,str(i)))
        if i<100:
            cnt += 1
        elif lst[0]-lst[1] == lst[1]-lst[2]:
            cnt += 1
    return cnt

cnt = hansu(N)
print(cnt)

# 내가 푼 풀이
N = int(input())

def hansu(N):
    cnt = 0
    for i in range(1,N+1):
        lst = list(map(int,str(i)))
        if lst[0]-lst[1] == lst[2]-lst[1]:
            cnt += 1
    return cnt

cnt = hansu(N)
print(cnt)

# 만약 4자리 숫자까지 포함한다면?
