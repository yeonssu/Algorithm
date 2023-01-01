def solution(flowers):
    lastday_list = []
    for i in range(len(flowers)):
        lastday_list.append(int(flowers[i][1]))
    lastday = max(lastday_list)
    
    cal = [0]*lastday

    for i in range(len(flowers)):
        a = int(flowers[i][0])
        b = int(flowers[i][1])

        while a < b:

            cal[a] = 1
            a += 1
    
    answer = cal.count(1)
    return answer

print(solution([[100,108],[78,90],[130,175],[200,203],[217,230],[245,290],[5,9],[350,365],[312,330]]))
print(solution([[3,4],[4,5],[6,7],[8,10]]))