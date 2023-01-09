def circle(N,lst):
    answer = []
    for i in range(N):
        new_lst = []
        for j in range(N):
            new_lst.append(lst[N-1-j][i])
        answer.append(new_lst)
    return answer

T = int(input())
for t in range(T):
    print("#"+str(t+1))
    N = int(input())
    lst = []
    for n in range(N):
        lst.append(list(map(int,input().split())))
    
    answer90 = circle(N,lst)
    # print(answer90)

    answer180 = circle(N,answer90)
    # print(answer180)

    answer270 = circle(N,answer180)
    # print(answer270)