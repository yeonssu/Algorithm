survey = ["TR", "RT", "TR"]
choices = [7,1,3]

def solution(survey, choices):
    R, T, C, F, J, M, A, N = 0, 0, 0, 0, 0, 0, 0, 0
    answer = ''
    num = len(survey)
    for i in range(0, num):
        if survey[i] == "RT":
            if choices[i] < 4:
                R = R + 4 - choices[i]
            else:
                T = T + choices[i] - 4
        elif survey[i] == "TR":
            if choices[i] < 4:
                T = T + 4 - choices[i]
            else:
                R = R + choices[i] - 4
        elif survey[i] == "CF":
            if choices[i] < 4:
                C = C + 4 - choices[i]
            else:
                F = F + choices[i] - 4
        elif survey[i] == "FC":
            if choices[i] < 4:
                F = F + 4 - choices[i]
            else:
                C = C + choices[i] - 4
        elif survey[i] == "JM":
            if choices[i] < 4:
                J = J + 4 - choices[i]
            else:
                M = M + choices[i] - 4
        elif survey[i] == "MJ":
            if choices[i] < 4:
                M = M + 4 - choices[i]
            else:
                J = J + choices[i] - 4
        elif survey[i] == "AN":
            if choices[i] < 4:
                A = A + 4 - choices[i]
            else:
                N = N + choices[i] - 4
        elif survey[i] == "NA":
            if choices[i] < 4:
                N = N + 4 - choices[i]
            else:
                A = A + choices[i] - 4
    if R >= T:
        answer += "R"
    else:
        answer += "T"
    if C >= F:
        answer += "C"
    else:
        answer += "F"
    if J >= M:
        answer += "J"
    else:
        answer += "M"
    if A >= N:
        answer += "A"
    else:
        answer += "N"
    return answer

answer = solution(survey, choices)
print(answer)