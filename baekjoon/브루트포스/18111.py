import sys
input = sys.stdin.readline
if __name__ == "__main__":
    N, M, B = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(N)]

    answer_time = 987654321
    answer_height = 0
    for height in range(257):
        inventory = B
        stacking = 0
        for i in range(N):
            for j in range(M):
                # 1번 작업 : 제거 2초
                if graph[i][j] > height:
                    inventory += (graph[i][j] - height)
                # 2번 작업 : 쌓기 1초
                else:
                    stacking += (height - graph[i][j])

        # 쌓아야 하는 개수가 인벤보다 많으면 불가능
        if stacking > inventory:
            continue

        time = 2 * (inventory - B) + stacking

        if time <= answer_time:
            answer_time = time
            answer_height = height

    print(answer_time, answer_height)
