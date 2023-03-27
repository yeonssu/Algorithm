# 시간 초과
# index 함수는 O(n)이므로 시간 초과 발생 -> index dict를 따로 만들어주어야한다
# 불필요한 graph 딕셔너리 -> 제거하자
# sales의 딕셔너리 값을 계속 수정하지말고 -> 리스트로 지정하자
def solution(enroll, referral, seller, amount):
    graph = dict()
    sales = dict()
    for enrol in enroll:
        sales[enrol] = 0
        # index 함수는 O(n)이므로 시간 초과 발생 -> index dict를 따로 만들어주어야한다
        i = enroll.index(enrol)
        while True:
            if referral[i] == "-":
                if graph.get(enrol) == None:
                    graph[enrol] = ["center"]
                else:
                    sub = graph.get(enrol)
                    sub.append("center")
                    graph[enrol] = sub
                break
            else:
                if graph.get(enrol) == None:
                    graph[enrol] = [referral[i]]
                else:
                    sub = graph.get(enrol)
                    sub.append(referral[i])
                    graph[enrol] = sub
                i = enroll.index(referral[i])
    print(graph)

    for i in range(len(seller)):
        price = amount[i] * 100
        sub = graph.get(seller[i])
        divide = len(sub)

        distribution = price * 10 // 100
        sales[seller[i]] = sales.get(seller[i]) + (price - distribution)
        price = distribution
        for j in range(divide - 1):
            distribution = price * 10 // 100
            sales[sub[j]] = sales.get(sub[j]) + (price - distribution)
            price = distribution

    answer = list(sales.values())
    print(answer)
    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10])
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"],
         [2, 3, 5, 4])
