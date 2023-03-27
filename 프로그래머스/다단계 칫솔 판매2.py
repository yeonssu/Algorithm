def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    idx = dict()
    for i, p in enumerate(enroll):
        idx[p] = i
    print(idx)
    for i in range(len(seller)):
        price = amount[i] * 100
        person = seller[i]
        while person != "-" and price > 0:
            distribution = price * 10 // 100
            answer[idx[person]] += price - distribution
            price = distribution
            person = referral[idx[person]]

    print(answer)
    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10])
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"],
         [2, 3, 5, 4])
