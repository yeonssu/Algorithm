import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
friends = [[N] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().strip().split())
    friends[A][B] = 1
    friends[B][A] = 1

for middle in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                friends[i][j] = 0
            else:
                if i != middle and j != middle:
                    friends[i][j] = min(friends[i][j], friends[i][middle] + friends[middle][j])

answers = []
for i in range(1, N + 1):
    answer = 0
    for j in range(1, N + 1):
        answer += friends[i][j]
    answers.append(answer)

print(answers.index(min(answers)) + 1)
