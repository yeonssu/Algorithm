import sys

input = sys.stdin.readline

N = int(input().strip())
scores = []

for n in range(N):
    name, korean, english, mathematics = input().strip().split()
    scores.append((name, int(korean), int(english), int(mathematics)))

scores = sorted(scores, key=lambda score: (-score[1], score[2], -score[3], score[0]))

for score in scores:
    print(score[0])
