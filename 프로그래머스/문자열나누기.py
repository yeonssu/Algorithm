def same_diff(word):
    print("====")
    print(word)
    x = word[0]
    same = 0
    diff = 0
    sub = ""
    for i in range(len(word)):
        if word[i] == x:
            same += 1
        else:
            diff += 1

        if same == diff:
            sub = word[i + 1:]
            break
    print(sub)
    return sub


def solution(s):
    answer = 0
    while True:
        s = same_diff(s)
        answer += 1
        if s == "":
            break
    return answer

solution("banana")
solution("abracadabra")
solution("aaabbaccccabba")