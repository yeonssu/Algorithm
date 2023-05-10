def solution(want, number, discount):
    answer = 0

    for i in range(len(discount) - 9):
        ten_list = discount[i:i + 10]
        print(ten_list)
        print(i)
        for j in range(len(want)):
            w = want[j]
            n = number[j]
            # 10개 자른 리스트에 존재하는 개수가 원하는 개수보다 작으면 종료
            if ten_list.count(w) < n:
                break
            else:
                if j == len(want) - 1:
                    answer += 1
        print(answer)

    return answer


solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
         ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
          "apple", "banana"])
solution(["apple"], [10],
         ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])
