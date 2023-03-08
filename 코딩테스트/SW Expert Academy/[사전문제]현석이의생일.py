import itertools
# 중복순열
def repeat(x,y,r):
    per = list(itertools.product([x,y], repeat=r))
    answer = []

    for ele in per:
        a = ""
        for i in range(len(ele)):
            a += str(ele[i])
        answer.append(int(a))
    return answer

def isInnerNum(num,max):
    if num>max:
        max = num
    return max
    
T = int(input())
for t in range(T):
    N, x, y = map(int,input().split())
    positional_number = len(str(N))
    result = [[x,y]]
    for j in range(2,positional_number+1):
            result.append(repeat(x,y,j))
    
    #이차원배열->일차원배열
    result = list(itertools.chain(*result))
    # print(result)

    max = -1
    for i in result:
        if i<=N and i!=0:
            max = isInnerNum(i,max)
    
    print("#" + str(t+1) + " " + str(max))


