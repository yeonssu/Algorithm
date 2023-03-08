def solution(today, terms, privacies):
    answer = []
    no_answer = []
    for i in range(len(privacies)):
        privacies_year = int(privacies[i][:4])
        privacies_month = int(privacies[i][5:7])
        privacies_day = int(privacies[i][8:10])
        typeform = privacies[i][-1:]
        
        for j in terms:
            if typeform == j[0]:
                plus_day = int(j[2:]) * 28

        result_day = privacies_day + plus_day

        Q1 = result_day // 28    # 몫 은 달에 추가
        R1 = result_day % 28     # 나머지 는 일
        if R1 == 0:
            result_month = privacies_month + Q1 - 1
            result_day = 28
        if result_day > 28:
            result_month = privacies_month + Q1
            result_day = R1

        Q2 = result_month // 12
        R2 = result_month % 12
        if result_month > 12:
            result_year = privacies_year + Q2
            result_month = R2
        else:
            result_year = privacies_year
        
        print(result_year,result_month, result_day)

        today_year = int(today[:4])
        today_month = int(today[5:7])
        today_day = int(today[8:])

        if today_year > result_year:
            answer.append(i+1)
        elif today_year < result_year:
            no_answer.append(i+1)
        else:
            if today_month > result_month:
                answer.append(i+1)
            elif today_month < result_month:
                no_answer.append(i+1)
            else:
                if today_day >= result_day:
                    answer.append(i+1)
                else:
                    no_answer.append(i+1)

    return answer

# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result = solution(today, terms, privacies)

today = "2020.01.01"
terms = ["Z 27", "D 5"]
privacies = ["2019.01.01 Z", "2019.11.15 Z", "2019.08.02 Z", "2019.07.01 Z", "2018.12.28 Z"]
result = solution(today, terms, privacies)
print(result)
