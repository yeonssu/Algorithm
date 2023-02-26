import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

paper = []
for n in range(N):
    paper.append(list(map(int, input().strip().split())))


def choose_tetromino_type(type, start_x, start_y):
    if type == 1:  # blue
        return [(start_x, start_y), (start_x + 1, start_y), (start_x + 2, start_y), (start_x + 3, start_y)]
    if type == 2:  # yellow
        return [(start_x, start_y), (start_x + 1, start_y), (start_x, start_y + 1), (start_x + 3, start_y + 1)]
    if type == 3:  # orange
        return [(start_x, start_y), (start_x, start_y + 1), (start_x, start_y + 2), (start_x + 1, start_y + 2)]
    if type == 4:  # green
        return [(start_x, start_y), (start_x, start_y + 1), (start_x + 1, start_y + 1), (start_x + 1, start_y + 2)]
    if type == 5:  # pink
        return [(start_x, start_y), (start_x + 1, start_y), (start_x + 2, start_y), (start_x + 1, start_y + 1)]



for x in range(N):
    for y in range(M):
        score = 0
        for type in range(1, 5):
            xylist = choose_tetromino_type(type, x, y)
            print(xylist)
            for y, x in xylist:
                if 0 <= x < M and 0 <= y < M:
                    print(paper[x][y])
                    score += paper[x][y]
                else:
                    score = 0
                    break
            # print("type", type)
            # print("score", score)
