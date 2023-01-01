N = int(input())

real_score = list(map(int, input().split()))
M = max(real_score)
false_score = []
for s in real_score:
    false_score.append(s/M*100)

avg = sum(false_score)/N
print(avg)