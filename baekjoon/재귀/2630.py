import sys

input = sys.stdin.readline
N = int(input().strip())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().strip().split())))

white_cnt = 0
blue_cnt = 0


def divide(x, y, N):
    global white_cnt, blue_cnt
    first_color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if first_color != paper[i][j]:
                divide(x, y, N // 2)
                divide(x, y + N // 2, N // 2)
                divide(x + N // 2, y, N // 2)
                divide(x + N // 2, y + N // 2, N // 2)
                return
    if first_color == 1:
        blue_cnt += 1
    else:
        white_cnt += 1


divide(0, 0, N)
print(white_cnt)
print(blue_cnt)
