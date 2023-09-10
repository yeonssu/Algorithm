import sys

input = sys.stdin.readline


def plus_zero(arr):
    max_cnt = 3
    for i in range(len(arr)):
        max_cnt = max(max_cnt, len(arr[i]))

    if max_cnt >= 100:
        for i in range(len(arr)):
            arr[i] = arr[i][:100]
    else:
        for i in range(len(arr)):
            arr[i].extend([0] * (max_cnt - len(arr[i])))
    return arr


def r_operation(arr):
    new = []
    for i in range(len(arr)):
        sub = set()
        for a in arr[i]:
            if a != 0:
                sub.add((a, arr[i].count(a)))
        sub = list(sub)
        sub.sort(key=lambda x: (x[1], x[0]))
        new.append([el for s in sub for el in s])
    return plus_zero(new)


def c_operation(arr):
    n = len(arr)  # 행 길이 계산
    m = len(arr[0])  # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = arr[i][j]

    arr = r_operation(new)
    n = len(arr)  # 행 길이 계산
    m = len(arr[0])  # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                new[j][i] = arr[i][j]
    return new


def r_or_c(arr):
    r_cnt = len(arr)
    c_cnt = len(arr[0])
    if r_cnt >= c_cnt:
        return r_operation(arr)
    else:
        return c_operation(arr)


if __name__ == "__main__":
    r, c, k = map(int, input().strip().split())
    A = [list(map(int, input().strip().split())) for i in range(3)]
    time = 0
    try:
        flag = A[r - 1][c - 1] != k
    except IndexError:
        flag = True
    while flag:
        time += 1
        A = r_or_c(A)
        try:
            flag = A[r - 1][c - 1] != k
        except IndexError:
            flag = True
        if time > 100:
            time = -1
            break

    print(time)
