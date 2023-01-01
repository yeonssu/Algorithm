from math import *

def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        rest_day = ceil((100 - progresses[i])/speeds[i])
        day.append(rest_day)

    result_day = []
    result_day.append(day[0])
    a = 0
    for i in range(1,len(day)):
        if result_day[a] > day[i]:
            result_day.append(result_day[a])
        else:
            result_day.append(day[i])
        a += 1
    print(result_day)

    answer = []
    cnt = 1
    for i in range(1,len(result_day)):
        if result_day[i-1] == result_day[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer



# 5 10 1 1 20 1
# 5 10 10 10 20 20
# 1 3 2
