def solution(cards1, cards2, goal):
    answer = 'Yes'
    i, j = 0, 0
    for g in goal:
        if i < len(cards1) and g == cards1[i]:
            i += 1
        elif j < len(cards2) and g == cards2[j]:
            j += 1
        else:
            answer = 'No'
            break

    return answer


solution(["i", "water", "drink"],	["want", "to"],	["i", "want", "to", "drink", "water"])
solution(["i", "drink", "water"],	["want", "to"],	["i", "want", "to", "drink", "water"])
