def solution(dartResult):
    numbers = []
    i = 0
    while i < len(dartResult):
        result = ""
        while dartResult[i].isdigit():
            result += dartResult[i]
            i += 1
        if result.isdigit():
            score = int(result)
            bonus = dartResult[i]
            if bonus == "S":
                numbers.append(score)
            elif bonus == "D":
                numbers.append(score * score)
            elif bonus == "T":
                numbers.append(score * score * score)
        else:
            option = dartResult[i]
            if option == "*":
                numbers[-1] *= 2
                if len(numbers) >= 2:
                    numbers[-2] *= 2
            elif option == "#":
                numbers[-1] *= (-1)
        i += 1
    return sum(numbers)


solution("1S2D*3T")
solution("1D2S#10S")
solution("1D2S0T")
solution("1S*2T*3S")
solution("1D#2S*3S")
solution("1T2D3D#")
solution("1D2S3T*")