def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        flag = True
        continuous = {"aya": False, "ye": False, "woo": False, "ma": False}
        i = 0
        while i < len(word):
            if word[i:i + 3] == "aya" and not continuous.get("aya"):
                i += 3
                continuous = {"aya": True, "ye": False, "woo": False, "ma": False}
            elif word[i:i + 2] == "ye" and not continuous.get("ye"):
                i += 2
                continuous = {"aya": False, "ye": True, "woo": False, "ma": False}
            elif word[i:i + 3] == "woo" and not continuous.get("woo"):
                i += 3
                continuous = {"aya": False, "ye": False, "woo": True, "ma": False}
            elif word[i:i + 2] == "ma" and not continuous.get("ma"):
                i += 2
                continuous = {"aya": False, "ye": False, "woo": False, "ma": True}
            else:
                flag = False
                break
        if flag:
            answer += 1

    return answer


solution(["ayawooaya"])
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
solution(["aya", "yee", "u", "maa"])
