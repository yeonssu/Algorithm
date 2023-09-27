import sys
from collections import deque
from itertools import permutations


input = sys.stdin.readline


def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append((start_x, start_y))
    visited = [[0] * w for _ in range(h)]
    visited[start_y][start_x] = 1
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and room[ny][nx] != "x":
                que.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1

    return visited



if __name__ == "__main__":
    while True:
        w, h = map(int, input().strip().split())
        if w == 0 and h == 0:
            exit()
        room = [list(map(str, input().strip())) for _ in range(h)]
        start = (0, 0)
        dirty = []
        for i in range(h):
            for j in range(w):
                if room[i][j] == "o":
                    start = (j, i)
                elif room[i][j] == "*":
                    dirty.append((j, i))
        visited = bfs(start[0], start[1])
        cleaner = [0] * len(dirty)
        flag = True
        for i in range(len(dirty)):
            x, y = dirty[i][0], dirty[i][1]
            if not visited[y][x]:
                print(-1)
                flag = False
                break

            cleaner[i] = (visited[y][x] - 1)

        if flag:
            distance = [[0] * (len(dirty)) for _ in range(len(dirty))]
            for i in range(len(dirty) - 1):
                visited = bfs(dirty[i][0], dirty[i][1])
                for j in range(i + 1, len(dirty)):
                    distance[i][j] = visited[dirty[j][1]][dirty[j][0]] - 1
                    distance[j][i] = distance[i][j]
            answer = 987654321
            for li in permutations(range(len(distance))):
                temp = cleaner[li[0]]
                start = li[0]
                for idx in range(1, len(li)):
                    end = li[idx]
                    temp += distance[start][end]
                    start = end
                answer = min(answer, temp)
            print(answer)
