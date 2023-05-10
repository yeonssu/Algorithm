def solution1(n, left, right):
    answer = []
    for i in range(n * n):
        a = i // n
        b = i % n
        value = max(a, b)
        answer.append(value + 1)

    return answer[left:right + 1]


def solution2(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        value = max(a, b)
        answer.append(value + 1)

    return answer


solution1(3, 2, 5)
solution1(4, 7, 14)
solution2(3, 2, 5)
solution2(4, 7, 14)
