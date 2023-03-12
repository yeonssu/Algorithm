def solution(today, terms, privacies):
    answer = []

    today_year, today_month, today_day = today.split(".")
    today_total_day = int(today_year) * 336 + int(today_month) * 28 + int(today_day)

    terms_dict = dict()
    for term in terms:
        type, duration = term.split(" ")
        terms_dict[type] = int(duration)

    for i in range(len(privacies)):
        personal_info, choose_term = privacies[i].split(" ")
        year, month, day = personal_info.split(".")
        total_day = int(year) * 336 + int(month) * 28 + int(day)
        choose_duration = terms_dict.get(choose_term)
        total_day += choose_duration * 28

        if today_total_day >= total_day:
            answer.append(i + 1)

    print(answer)
    return answer


solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])