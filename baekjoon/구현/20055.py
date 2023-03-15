import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().strip().split())

durability = deque(map(int, input().strip().split()))
robot = deque(False for _ in range(N))

answer = 0
while durability.count(0) < K:
    # 벨트 이동
    durability.rotate(1)
    robot.rotate(1)
    robot[0] = False

    # 로봇 이동
    for i in reversed(range(len(robot))):
        # 로봇이 내리는 위치에 도달하면 그 즉시 내린다
        if i == len(robot) - 1:
            robot[i] = False
            break
        # 가장 먼저 벨트에 올라간 로봇부터
        if robot[i]:
            # 만약 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다
            # 다음 칸에 로봇이 없고, 그 칸의 내구도가 1 이상이어야 이동 가능
            if i + 1 < len(robot) and not robot[i + 1] and durability[i + 1] >= 1:
                durability[i + 1] -= 1
                robot[i] = False
                robot[i + 1] = True

    # 새로운 로봇 추가
    if durability[0] > 0:
        durability[0] -= 1
        robot[0] = True

    answer += 1

print(answer)
