import sys
from collections import defaultdict
input = sys.stdin.readline


# 좋아하는 학생이 많은 칸 > 비어있는 칸이 많은 칸 > 행의 번호가 가장 작은 칸 > 열의 번호가 가장 작은 칸
if __name__ == "__main__":
    N = int(input().strip())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    classroom = [[0] * N for _ in range(N)]
    favorite = defaultdict(list)
    for _ in range(N * N):
        a, b, c, d, e = map(int, input().strip().split())
        favorite[a] = [b, c, d, e]
    for student in favorite.keys():
        friends = favorite.get(student)
        possible_seat = []
        for y in range(N):
            for x in range(N):
                like = 0
                blank = 0
                if classroom[y][x] == 0:
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if classroom[ny][nx] in friends:
                                like += 1
                            if classroom[ny][nx] == 0:
                                blank += 1
                    possible_seat.append((like, blank, x, y))
        possible_seat.sort(key=lambda x: (-x[0], -x[1], x[3], x[2]))
        like, blank, x, y = possible_seat[0]
        classroom[y][x] = student

    # 좋아하는 학생의 수 0 : 만족도 0
    # 좋아하는 학생의 수 1 : 만족도 1
    # 좋아하는 학생의 수 2 : 만족도 10
    # 좋아하는 학생의 수 3 : 만족도 100
    # 좋아하는 학생의 수 4 : 만족도 1000
    result = 0
    for student in range(1, N * N + 1):
        friends = favorite.get(student)
        for y in range(N):
            for x in range(N):
                if classroom[y][x] == student:
                    cnt = 0
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if classroom[ny][nx] in friends:
                                cnt += 1
                    if cnt == 1:
                        result += 1
                    elif cnt == 2:
                        result += 10
                    elif cnt == 3:
                        result += 100
                    elif cnt == 4:
                        result += 1000

    print(result)
