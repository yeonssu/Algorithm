# 테스트 케이스 불통
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    for r in reserve:
        for l in lost:
            if r - 1 == l:
                answer += 1
                break
            elif r + 1 == l:
                answer += 1
                break
    return answer


def solution2(n, lost, reserve):
    reserve_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)
    answer = n - len(lost_del)
    for r in reserve_del:
        if r - 1 in lost_del:
            lost_del.remove(r - 1)
        elif r + 1 in lost_del:
            lost_del.remove(r + 1)
    return answer


print(solution2(5, [2, 4], [1, 3, 5]))
print(solution2(5, [2, 4], [3]))
print(solution2(3, [3], [1]))
