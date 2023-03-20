def move(box, cap, n):
    delivery = cap
    for i in range(n - 1, -1, -1):
        if box[i] != 0:
            if delivery - box[i] > 0:
                delivery -= box[i]
                box[i] = 0
            else:
                box[i] -= delivery
                break


def solution(cap, n, deliveries, pickups):
    answer = 0
    while n > 0:
        while n > 0 and deliveries[n - 1] == 0 and pickups[n - 1] == 0:
            n -= 1

        move(deliveries, cap, n)
        move(pickups, cap, n)
        answer += n * 2

    return answer


solution(2, 7, [1, 0, 2, 0, 1, 0, 0], [0, 2, 0, 1, 0, 0, 0])
solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])  # 30
solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])  # 16

'''
갈 때는 남은 배달이 있는 최대한 먼 집까지 가는데
돌아올 때는 남은 수거가 있는 최대한 먼 집부터 수거를 한다
'''
