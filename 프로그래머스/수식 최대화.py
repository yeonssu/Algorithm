from itertools import permutations


def solution(expression):
    answer = 0
    i = 0
    numbers = []
    operators = []
    sub = ""
    while i <= len(expression):
        if i == len(expression):
            numbers.append(int(sub))
        elif expression[i].isdigit():
            sub += expression[i]
        else:
            if sub != "":
                numbers.append(int(sub))
                sub = ""
            operators.append(expression[i])
        i += 1

    priority = permutations(set(operators))
    for op in priority:
        number = numbers.copy()
        operator = operators.copy()
        for o in op:
            i = 0
            while i < len(operator):
                if operator[i] == o and i + 1 < len(number):
                    displace = eval(str(number[i]) + o + str(number[i + 1]))
                    number[i] = displace
                    number.remove(number[i + 1])
                    operator.remove(operator[i])
                    i -= 1
                i += 1
        answer = max(answer, abs(number[0]))
    return answer


print(solution("50*6-3*2"))  # 300
print(solution("100-200*300-500+20"))  # 60420
