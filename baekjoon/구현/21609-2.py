from collections import deque
import sys


# 블록 그룹 조건
# [조건 1] 일반 블록 적어도 하나 이상 -> 일반 블록을 기준으로 bfs를 돌아야한다
# [조건 2] 일반 블록인 경우, 색이 같아야한다
# [조건 3] 검은 색 블록 포함 X
# [조건 4] 무지개는 얼마나 들어있든 상관 없음
# [조건 5] 총 블록 개수는 2보다 크거나 같다
# [조건 6] 모든 블록이 인접한 칸 조건을 만족해야한다 (인접한 칸 : |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸 (r1, c1)과 (r2, c2) -> 양 옆 위 아래)
def bfs(x, y, color):
    que = deque()
    que.append((x, y))
    # [조건 6] 모든 블록이 인접한 칸 조건을 만족해야한다
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 일반 블록
    general_block_cnt = 1
    general_blocks = [(x, y)]

    # 무지개 블록
    rainbow_block_cnt = 0
    rainbow_blocks = []

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위 안에 있을 때
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # [조건 2] 일반 블록인 경우, 색이 같아야한다
                if graph[nx][ny] == color:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    general_block_cnt += 1
                    general_blocks.append((nx, ny))
                # [조건 4] 무지개는 얼마나 들어있든 상관 없음
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    rainbow_block_cnt += 1
                    rainbow_blocks.append((nx, ny))
                # [조건 3] 검은 색 블록 포함 X
                elif graph[nx][ny] == -1:
                    continue

    # [조건 4] 무지개는 얼마나 들어있든 상관 없음 -> 무지개 블록은 방문 해제
    for x, y in rainbow_blocks:
        visited[x][y] = False

    return [general_block_cnt + rainbow_block_cnt, rainbow_block_cnt, general_blocks + rainbow_blocks]


# 블록 제거
def remove_block(block_group):
    for x, y in block_group:
        graph[x][y] = -2


# 중력 : 모든 블록이 행의 번호가 큰 칸으로 이동 -> 가장 아래의 칸으로 몰리게 떨어짐
def gravity(graph):
    for y in reversed(range(N - 1)):
        for x in range(N):
            # 검은색 블록을 제외한 비어있지 않은 곳
            if graph[y][x] > -1:
                down = y
                while True:
                    # 다음 칸이 비어있는 칸이면 계속 내리기
                    if 0 <= down + 1 < N and graph[down + 1][x] == -2:
                        graph[down + 1][x], graph[down][x] = graph[down][x], graph[down + 1][x]
                        down += 1
                    # 다음 칸이 비어있지 않으면 바꾸지 않고 종료
                    else:
                        break


# 반시계 회전
def rotate(graph):
    new_graph = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_graph[N - 1 - x][y] = graph[y][x]
    return new_graph


input = sys.stdin.readline

# N : 격자 크기 / M : 색상 개수
# 블록 : 검은색 -1 / 무지개 0 / 일반 숫자
N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]

result = 0
# 1️⃣ 오토플레이
while True:
    # 2️⃣ 크기가 가장 큰 블록 그룹 찾기
    visited = [[False] * N for _ in range(N)]
    block_group = []
    for i in range(N):
        for j in range(N):
            # [조건 1] 일반 블록 적어도 하나 이상
            if not visited[i][j] and graph[i][j] > 0:
                visited[i][j] = True
                # bfs에서 (총 블록 개수, 무지개 블록 개수, 블록 그룹 좌표값)를 받는다
                t_cnt, r_cnt, block_x_y = bfs(i, j, graph[i][j])
                # 기준 블록 : 무지개 블록이 아닌 블록 중 [행이 가장 작은 > 열이 가장 작은]
                # -> bfs를 시작하는 블록을 기준 블록으로 잡는다
                standard_block = [j, i]

                # [조건 5] 총 블록 개수는 2보다 크거나 같다
                if t_cnt >= 2:
                    # (블록 개수가 가장 많은 그룹 > 무지개 블록 수가 가장 많은 그룹 > 기준 블록의 행이 가장 큰 것 > 기준 블록의 열이 가장 큰 것) 기준으로 정렬이므로
                    # block_group에 블록 개수, 무지개 블록 수, 기준 블록 행, 기준 블록 열, 블록 좌표값
                    block_group.append([t_cnt, r_cnt, standard_block[1], standard_block[0], block_x_y])

    block_group.sort(reverse=True)

    # 3️⃣ 블록 그룹이 없으면 종료
    if not block_group:
        break

    # 4️⃣ 블록 제거
    remove_block(block_group[0][4])

    # 5️⃣ 점수 더하기
    result += block_group[0][0] ** 2

    # 6️⃣ 중력
    gravity(graph)

    # 7️⃣ 회전
    graph = rotate(graph)

    # 8️⃣ 중력
    gravity(graph)

print(result)
