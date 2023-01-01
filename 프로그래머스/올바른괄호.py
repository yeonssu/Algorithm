def solution(s):
    lst = []

    if s[0] == ")":
        return False

    for i in range(len(s)):
        if s[i] == "(":
            lst.append(s[i])
        else:
            if len(lst) == 0:
                return False
            lst.pop()

    if len(lst) == 0:
        return True
    else:
        return False