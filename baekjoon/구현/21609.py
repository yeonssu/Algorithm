from collections import deque
import sys

input = sys.stdin.readline

# N : 격자 크기 / M : 색상 개수
N, M = map(int, input().strip().split())
graph = []
for n in range(N):
    graph.append(list(map(int, input().strip().split())))

for p in graph:
    print(p)

# 블록 : 검은색 -1 / 무지개 0 / 일반 숫자
# 인접한 칸 : |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸 (r1, c1)과 (r2, c2)
# 블록 그룹 조건
# 1. 일반 블록 적어도 하나 이상
# 2. 일반 블록 색 모두 같아야 한다
# 3. 검은 색 블록 포함 X
# 4. 무지개는 상관 없음
# 5. 총 블록 개수는 2보다 크거나 같다
# 6. 모든 블록이 인접한 칸 조건을 만족해야한다
# 기준 블록 : 무지개 블록이 아닌 블록 중 행이 가장 작은 > 열이 가장 작은
# 게임 기준

block = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 가장 큰 블록 그룹 찾기
# 개수가 가장 많은 그룹 > 무지개 블록 수가 가장 많은 그룹 > 기준 블록의 행이 가장 큰 것 > 기준 블록의 열이 가장 큰 것
def search_biggest_block_group():
    while block:
        x, y = block.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]


# 중력 : 모든 블록이 행의 번호가 큰 칸으로 이동 -> 가장 아래의 칸으로 몰리게 떨어짐
def gravity():
    for x in range(N):
        vertical = deque()
        ground = deque()
        for y in range(N - 1, -1, -1):
            if graph[y][x] != M + 1 and graph[y][x] != -1:
                vertical.append((y, graph[y][x]))
            if graph[y][x] == -1:
                ground.append(y)

        if len(ground) == 0:
            ground.append(5)


        print("===========================")
        print(vertical)
        print(ground)

        while vertical:
            yy, value = vertical.popleft()
            while len(ground) >= 2:
                end, start = ground.popleft(), ground[0]
                print("** start : " + str(start))
                for move_y in reversed(range(start + 1, end)):
                    print(move_y)
                    if graph[move_y][x] == M + 1:
                        graph[move_y][x] = value
                        graph[yy][x] = M + 1
                        break

                print("** end : " + str(end))





# 반시계 회전
# def lotation():


# for i in range(N):
#     for j in range(N):
#         graph[i][j]
gravity()
for p in graph:
    print(p)
