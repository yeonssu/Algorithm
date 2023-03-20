from itertools import product


def solution(users, emoticons):
    discounts = [40, 30, 20, 10]
    discounts = list(product(discounts, repeat=len(emoticons)))
    answer = [0, 0]
    for discount in discounts:  # discount = (40,40)
        emoticon_plus_service = 0
        emoticon_total_sale_price = 0
        for user in users:  # user = [40, 10000]
            user_purchase_amount = 0
            for i in range(len(emoticons)):
                if discount[i] >= user[0]:
                    user_purchase_amount += emoticons[i] * (100 - discount[i]) // 100
            # 플러스 가입 x
            if user[1] > user_purchase_amount:
                emoticon_total_sale_price += user_purchase_amount
            # 플러스 가입 o
            else:
                emoticon_plus_service += 1

        if answer[0] < emoticon_plus_service:
            answer[0] = emoticon_plus_service
            answer[1] = emoticon_total_sale_price
        elif answer[0] == emoticon_plus_service:
            if answer[1] < emoticon_total_sale_price:
                answer[0] = emoticon_plus_service
                answer[1] = emoticon_total_sale_price

    return answer


solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
solution([[40, 10000], [25, 10000]], [7000, 9000])
