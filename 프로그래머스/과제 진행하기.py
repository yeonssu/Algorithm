def solution(plans):
    answer = []
    not_finish = []

    sorted_plans = []
    for plan in plans:
        subject = plan[0]
        start_hr, start_min = plan[1].split(":")
        start = int(start_hr) * 60 + int(start_min)
        end = start + int(plan[2])
        sorted_plans.append([subject, start, end])
    sorted_plans = sorted(sorted_plans, key=lambda x: x[1])
    print(sorted_plans)

    for i in range(len(sorted_plans)):
        subject, start, end = sorted_plans[i]
        if i + 1 < len(sorted_plans):
            next_subject, next_start, next_end = sorted_plans[i + 1]
            # 그 전에 다 끝나는 경우
            if end <= next_start:
                answer.append(subject)
                left_time = next_start - end
                while len(not_finish) > 0:
                    sub, time = not_finish.pop()
                    # 남은 시간이 적어서 과목들을 못 끝낸 경우
                    if left_time < time:
                        not_finish.append([sub, time - left_time])
                        break
                    # 남은 시간이 많아서 다 끝낸 경우
                    else:
                        answer.append(sub)
                        left_time -= time
            # 전에 다 끝나지 못하는 경우
            else:
                not_finish.append([subject, end - next_start])
        if i == len(sorted_plans) - 1:
            answer.append(subject)
            while len(not_finish) > 0:
                sub, time = not_finish.pop()
                answer.append(sub)
    print(answer)
    return answer


solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])
solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])
solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])
