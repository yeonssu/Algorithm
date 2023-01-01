survey = ["TR", "RT", "TR"]
choices = [7,1,3]

def solution(survey, choices):
    R, T, C, F, J, M, A, N = 0, 0, 0, 0, 0, 0, 0, 0
    num = len(survey)
    for i in range(0, num):
        if survey[i] == "RT":
            if choices[i] == 1:
                R += 3
            elif choices[i] == 2:
                R += 2
            elif choices[i] == 3:
                R += 1
            else:
                T = T + choices[i] - 4
        elif survey[i] == "TR":
            if choices[i] == 1:
                T += 3
            elif choices[i] == 2:
                T += 2
            elif choices[i] == 3:
                T += 1
            else:
                R = R + choices[i] - 4
        elif survey[i] == "CF":
            if choices[i] == 1:
                C += 3
            elif choices[i] == 2:
                C += 2
            elif choices[i] == 3:
                C += 1
            else:
                F = F + choices[i] - 4
        elif survey[i] == "FC":
            if choices[i] == 1:
                F += 3
            elif choices[i] == 2:
                F += 2
            elif choices[i] == 3:
                F += 1
            else:
                C = C + choices[i] - 4
        elif survey[i] == "JM":
            if choices[i] == 1:
                J += 3
            elif choices[i] == 2:
                J += 2
            elif choices[i] == 3:
                J += 1
            else:
                M = M + choices[i] - 4
        elif survey[i] == "MJ":
            if choices[i] == 1:
                M += 3
            elif choices[i] == 2:
                M += 2
            elif choices[i] == 3:
                M += 1
            else:
                J = J + choices[i] - 4
        elif survey[i] == "AN":
            if choices[i] == 1:
                A += 3
            elif choices[i] == 2:
                A += 2
            elif choices[i] == 3:
                A += 1
            else:
                N = N + choices[i] - 4
        elif survey[i] == "NA":
            if choices[i] == 1:
                N += 3
            elif choices[i] == 2:
                N += 2
            elif choices[i] == 3:
                N += 1
            else:
                A = A + choices[i] - 4
    result = []
    if R >= T:
        result.append("R")
    else:
        result.append("T")
    if C >= F:
        result.append("C")
    else:
        result.append("F")
    if J >= M:
        result.append("J")
    else:
        result.append("M")
    if A >= N:
        result.append("A")
    else:
        result.append("N")
    str_result = "".join(result)
    answer = str_result
    return answer

answer = solution(survey, choices)
print(answer)