import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
students = [[False] * (N + 1) for _ in range(N + 1)]

# a가 b보다 작다
for m in range(M):
    a, b = map(int, input().strip().split())
    students[a][b] = True

for middle in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            else:
                if i != middle and j != middle:
                    if students[i][middle] and students[middle][j]:
                        students[i][j] = True

answer = 0
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if students[i][j] or students[j][i]:
            cnt += 1
    if cnt == N - 1:
        answer += 1

print(answer)
