def solution(x):
    lenth = len(str(x))
    x_list = list(map(int,str(x)))
    sum = 0
    for i in range(lenth):
        sum += x_list[i]
    if x%sum == 0:
        answer = True
    else:
        answer = False    
    return answer
Result = solution(18)
print(Result)