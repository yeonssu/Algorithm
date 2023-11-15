import sys
input = sys.stdin.readline


def rotate(sticker):
    new_sticker = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_sticker[j][r - i - 1] = sticker[i][j]
    return new_sticker


def search_space(r, c, sticker):
    sticker_coordinates = get_sticker_coordinates(r, c, sticker)
    for coordinates in sticker_coordinates:
        possible = True
        for x, y in coordinates:
            if notebook[y][x] == 1:
                possible = False
                break
        if possible:
            return coordinates
    return None


def get_sticker_coordinates(r, c, sticker):
    # (스티커 가로 > 노트북 가로) or (스티커 세로 > 노트북 세로) 불가능
    if r > n or c > m:
        return []
    # 스티커 붙일 수 있는 노트북 공간의 좌표
    sticker_coordinates = []
    for i in range(n - r + 1):
        for j in range(m - c + 1):
            sub = []
            for y in range(r):
                for x in range(c):
                    if sticker[y][x] == 1:
                        sub.append((j + x, i + y))
            # 가장 위쪽에 위치한 것 -> 가장 왼쪽에 위치한 것
            sticker_coordinates.append(sorted(sub, key=lambda x: (x[1], x[0])))
    return sticker_coordinates


if __name__ == "__main__":
    n, m, k = map(int, input().strip().split())
    notebook = [[0] * m for _ in range(n)]
    for _ in range(k):
        r, c = map(int, input().strip().split())
        sticker = [list(map(int, input().strip().split())) for _ in range(r)]
        result = search_space(r, c, sticker)
        for _ in range(4):
            if result is None:
                sticker = rotate(sticker)
                r = len(sticker)
                c = len(sticker[0])
                result = search_space(r, c, sticker)
            else:
                while result:
                    x, y = result.pop()
                    notebook[y][x] = 1
                break

    cnt = 0
    for i in range(n):
        for j in range(m):
            if notebook[i][j] == 1:
                cnt += 1
    print(cnt)
