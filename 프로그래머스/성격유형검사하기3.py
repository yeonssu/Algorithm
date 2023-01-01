survey = ["TR", "RT", "TR"]
choices = [7,1,3]

def solution(survey, choices):
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    answer = ''
    num = len(survey)
    for i in range(num):
        if choices[i] < 4:
            dic[survey[i][0]] = dic[survey[i][0]] + 4 - choices[i]
        else:
            dic[survey[i][1]] = dic[survey[i][1]] + choices[i] - 4
    
    lst = ["RT", "CF", "JM", "AN"]
    for i in range(len(lst)):
        if dic[lst[i][0]] >= dic[lst[i][1]]:
            answer += lst[i][0]
        else:
            answer += lst[i][1]
    return answer

answer = solution(survey, choices)
print(answer)