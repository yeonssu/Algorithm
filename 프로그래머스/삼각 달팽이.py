def solution(n):
    answer = [[0 for j in range(i)] for i in range(1, n + 1)]
    x, y = 0, -1
    num = 1
    for direction in range(n):
        for j in range(direction, n):
            # 아래쪽
            if direction % 3 == 0:
                dx = 0
                dy = 1
            # 오른쪽
            elif direction % 3 == 1:
                dx = 1
                dy = 0
            # 위쪽
            else:
                dx = -1
                dy = -1
            x += dx
            y += dy
            answer[y][x] = num
            num += 1
    print(answer)
    return sum(answer, [])


solution(4)  # [1,2,9,3,10,8,4,5,6,7]
solution(5)  # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
solution(6)  # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
