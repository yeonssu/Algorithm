# 구현
def solution(merchantNames):
    answer = []
    # 공백을 제외하고 가장 긴 텍스트
    # 특수 문자가 있다면 포함된 경우
    for name in merchantNames:
        if ["&", "(", ")", ".", "," "-"] in name:
            break

    return answer


solution(["토스커피사일로&베이커리", "토스커피사일로 베이커리", "토스커피사일로 베이커", "토스커피사일로 베이", "토스커피사일", "비바리퍼블리카 식당", "비바리퍼블리카식", "비바리퍼블리"])
