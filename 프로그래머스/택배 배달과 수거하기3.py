def solution(cap, n, deliveries, pickups):
    answer = 0

    have_to_deli = cap
    have_to_pick = cap

    for i in range(n - 1, -1, -1):
        have_to_deli -= deliveries[i]
        have_to_pick -= pickups[i]

        if have_to_deli <= 0 or have_to_pick <= 0:
            answer += (i + 1) * 2

    print(answer)
    return answer


solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])  # 30
solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])  # 16

'''
갈 때는 남은 배달이 있는 최대한 먼 집까지 가는데
돌아올 때는 남은 수거가 있는 최대한 먼 집부터 수거를 한다
'''
