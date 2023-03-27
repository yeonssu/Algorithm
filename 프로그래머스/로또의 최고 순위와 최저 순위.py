def winner(result):
    if result == 0 or result == 1:
        return 6
    elif result == 2:
        return 5
    elif result == 3:
        return 4
    elif result == 4:
        return 3
    elif result == 5:
        return 2
    elif result == 6:
        return 1


def solution(lottos, win_nums):
    answer = []
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)

    min_result = 0
    max_result = 0
    for lotto in lottos:
        if lotto == 0:
            max_result += 1
        for win_num in win_nums:
            if lotto == win_num:
                min_result += 1
                max_result += 1
                break

    answer.append(winner(max_result))
    answer.append(winner(min_result))
    return answer


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
