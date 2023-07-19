import sys

input = sys.stdin.readline
N = int(input().strip())
food = []
for n in range(N):
    food.append(list(map(str, input().strip().split()))[1:])
food.sort()
# [['APPLE', 'APPLE'], ['APPLE', 'BANANA', 'KIWI'], ['KIWI', 'APPLE'], ['KIWI', 'BANANA']]

for i in range(N):
    if i == 0:
        for j in range(len(food[i])):
            print("--" * j + food[i][j])

    else:
        idx = 0
        for j in range(len(food[i])):
            if food[i - 1][j] != food[i][j]:
                break
            else:
                idx = j + 1

        for j in range(idx, len(food[i])):
            print("--" * j + food[i][j])
