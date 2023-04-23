def solution(park, routes):
    answer = []
    move = {"E": [1, 0], "W": [-1, 0], "N": [0, -1], "S": [0, 1]}
    H = len(park)
    W = len(park[0])
    for y in range(H):
        for x in range(W):
            if park[y][x] == "S":
                for route in routes:
                    direction, length = route.split()
                    dx, dy = move.get(direction)
                    # 한 칸씩 이동하면서 장애물이 있는지 확인
                    for n in range(1, int(length) + 1):
                        nx = x + dx * n
                        ny = y + dy * n
                        # 벗어나거나 장애물을 만나면 다음 명령 실행
                        if nx < 0 or nx >= W or ny < 0 or ny >= H or park[ny][nx] == "X":
                            break
                        # 맨 마지막까지 공원을 벗어나지 않고 장애물을 만나지 않으면 이동
                        if n == int(length) and 0 <= nx < W and 0 <= ny < H and park[ny][nx] != "X":
                            x, y = nx, ny

                # 모든 이동이 끝나면 최종 위치 answer 에 추가
                answer.append(y)
                answer.append(x)
                break
    print(answer)

    return answer


solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])
solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"])
solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"])
