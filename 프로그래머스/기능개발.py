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
    
    answer = []
    for i in range(len(result_day)):
        cnt = result_day.count(result_day[i])
        if cnt not in answer:
            answer.append(cnt)

    return answer






def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            rest_day = (100 - progresses[i])//speeds[i]
        else:
            rest_day = (100 - progresses[i])//speeds[i] + 1
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
    
    answer = []
    for i in range(len(result_day)):
        cnt = result_day.count(result_day[i])
        if cnt not in answer:
            answer.append(cnt)

    return answer