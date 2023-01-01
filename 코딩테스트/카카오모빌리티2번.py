from collections import defaultdict

def solution(id_list, k):
    cnt = 0
    coupon = defaultdict(list)
    for i in range(len(id_list)):
        id = list(set(id_list[i].split()))
        for j in id:
            if coupon[j].count(1) < k:
                coupon[j].append(1)
    print(coupon)

    answer = 0
    for i in coupon:
        answer += coupon[i].count(1)
    print(answer)

    return answer

solution(["A B C D","A D", "A B D","B D"],2)
solution(["a","a b a c","c b c","b b b","c"],3)