import sys
input = sys.stdin.readline


def move(robot_x, robot_y, direction):
    if direction == "N":
        robot_y += 1
    elif direction == "W":
        robot_x -= 1
    elif direction == "E":
        robot_x += 1
    elif direction == "S":
        robot_y -= 1
    return (robot_x, robot_y)


def obey(robot_x, robot_y, order):
    rotation = ["N", "W", "S", "E"]
    robot, direction = board[robot_y][robot_x]
    board[robot_y][robot_x] = 0
    if order == "L":
        after = rotation.index(direction) + 1
        if after > 3:
            after = 0
        board[robot_y][robot_x] = (robot, rotation[after])
    elif order == "R":
        after = rotation.index(direction) - 1
        if after < 0:
            after = 3
        board[robot_y][robot_x] = (robot, rotation[after])
    elif order == "F":
        robot_x, robot_y = move(robot_x, robot_y, direction)
        if robot_x < 0 or robot_x >= A or robot_y < 0 or robot_y >= B:
            print("Robot " + str(robot) + " crashes into the wall")
            exit()
        elif board[robot_y][robot_x] != 0:
            print("Robot " + str(robot) + " crashes into robot " + str(board[robot_y][robot_x][0]))
            exit()
        board[robot_y][robot_x] = (robot, direction)
    return (robot_x, robot_y)


if __name__ == "__main__":
    # A : 가로 / B : 세로
    A, B = map(int, input().strip().split())
    board = [[0] * A for _ in range(B)]
    # N : 로봇 개수 / M : 명령 개수
    N, M = map(int, input().strip().split())
    robots = [0] * (N + 1)
    for robot in range(1, N + 1):
        x, y, direction = input().strip().split()
        x, y = int(x) - 1, int(y) - 1
        board[y][x] = (robot, direction)
        robots[robot] = (x, y)
    # 명령을 내리는 로봇 / 명령의 종류 / 반복 횟수
    # L : 왼쪽 90도 회전 / R : 오른쪽 90도 회전 / F : 앞으로 한 칸 움직
    for _ in range(M):
        robot, order, repeat = input().strip().split()
        robot, repeat = int(robot), int(repeat)
        x, y = robots[robot]
        for _ in range(repeat):
            x, y = obey(x, y, order)
            robots[robot] = (x, y)
    print("OK")