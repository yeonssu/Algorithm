from pickle import FALSE
from urllib.parse import urlencode


def solution(new_id):
    rule1 = new_id.lower()
    rule1 = list(rule1)
    print(rule1)

    rule2 = []
    for i in range(0,len(rule1)):
        if rule1[i].isalpha():
            rule2.append(rule1[i])
        elif rule1[i].isdigit():
            rule2.append(rule1[i])
        elif rule1[i] == "-" or rule1[i] == "_" or rule1[i] == ".":
            rule2.append(rule1[i])
    print(rule2)

    rule3 = []
    isDot = False
    for i in range(len(rule2)):
        if rule2[i] == ".":
            if isDot == False:
                rule3.append(rule2[i])
                isDot = True
            elif isDot == True:
                continue
        else:
            rule3.append(rule2[i])
            isDot = False
    print(rule3)
    
    if rule3[0] == "." and rule3[len(rule3)-1] == ".":
        if len(rule3) > 0:
            rule3.pop(len(rule3)-1)

        if len(rule3) > 0:
            rule3.pop(0)
    elif rule3[0] == "." and rule3[len(rule3)-1] != ".":
        rule3.pop(0)
    elif rule3[0] != "." and rule3[len(rule3)-1] == ".":
        rule3.pop(len(rule3)-1)
    rule4 = rule3    
    print(rule4)

    if len(rule4) == 0:
        rule4.append("aaa")
        print(rule4)
        answer_list = rule4
    elif len(rule4) == 1:
        rule4.append(rule4[len(rule4)-1],rule4[len(rule4)-1])
        print(rule4)
        answer_list = rule4
    elif len(rule4) == 2:
        rule4.append(rule4[len(rule4)-1])
        print(rule4)
        answer_list = rule4
    elif len(rule4) >= 16:
        rule6 = rule4[:15]
        if rule6[len(rule6)-1] == ".":
            rule6.pop(len(rule6)-1)
        print(rule6)
        answer_list = rule6
    else:
        answer_list = rule4

    answer = ''.join(str(s) for s in answer_list)
    return answer

Result = solution("...!@BaT#*..y.abcdefghijklm")
print(Result)
Result = solution("=.=")
print(Result)
Result = solution("123_.def")
print(Result)
Result = solution("abcdefghijklmn.p")
print(Result)
Result = solution("z-+.^.")
print(Result)