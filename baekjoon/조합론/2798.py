from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = []
for combi in combinations(cards, 3):
    if sum(combi) <= M:
        answer.append(sum(combi))
print(max(answer))
