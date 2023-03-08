def solution(s, times):
    y,m,d,hr,min,sec = s.split(":")
    print(y,m,d,hr,min,sec)

    for i in range(len(times)):
        day,hour,minute,second = times[i].split(":")

    answer = []
    return answer
print(solution("2021:04:12:16:08:35",["01:06:30:00","01:04:12:00"]))