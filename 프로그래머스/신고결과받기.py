def solution(id_list, report, k):
    warn_warned = []
    warn = []
    warned = []
    warning_list = []    

    for i in range(len(report)):
        a = report[i].split(" ")
        warn_warned.append(a)
        b,c = report[i].split()
        warn.append(b)
        warned.append(c)
    
    print(warn_warned,warn,warned)

    for i in range(len(id_list)):
        if warned.count(id_list[i]) >= k:
            warning_list.append(id_list[i])
    
    print(warning_list)

    answer = []    
    for i in range(len(warning_list)):
        d = warning_list[i]
        for j in range(len(warn_warned)):
            if d == warn_warned[j][1]:
                answer.append(id_list.index(warn_warned[j][0]))
    print(answer)
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)