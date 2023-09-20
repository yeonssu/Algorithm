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
        friends = list(favorite.get(student))
        possible_seat = []
        for i in range(N):
            for j in range(N):
                like = 0
                blank = 0
                if classroom[i][j] == 0:
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if classroom[ny][nx] in friends:
                                like += 1
                            if classroom[ny][nx] == 0:
                                blank += 1
                    possible_seat.append((like, blank, i, j))
        possible_seat.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
        like, blank, i, j = possible_seat[0]
        classroom[i][j] = student

    # 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
    # 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
    result = 0
    for student in range(1, N * N + 1):
        friends = favorite.get(student)
        for i in range(N):
            for j in range(N):
                if classroom[i][j] == student:
                    answer = 0
                    for k in range(4):
                        nx, ny = j + dx[k], i + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if classroom[ny][nx] in friends:
                                answer += 1
                    if answer != 0:
                        result += 10 ** (answer - 1)

    print(result)

