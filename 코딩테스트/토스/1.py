# 문자열
def solution(s, N):
    answer = 0
    sub = []
    for i in range(len(str(s)) - 1):
        substring = str(s)[i:i + N]
        for n in range(1, N + 1):
            if str(n) in substring:
                if n == N:
                    sub.append(substring)
                continue
            else:
                break
    if len(sub) == 0:
        return -1

    return int(max(sub))


solution(1451232125, 2)
solution(313253123, 3)
