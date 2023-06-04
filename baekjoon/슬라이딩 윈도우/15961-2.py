import sys
from collections import defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().strip().split())

sushi = []
for n in range(N):
    sushi.append(int(input().strip()))
sushi.extend(sushi)

eat = defaultdict(int)

eat[c] = 1

left = 0
result = 0
for right in range(len(sushi)):
    eat[sushi[right]] += 1

    if right > k - 1:
        eat[sushi[left]] -= 1
        if eat[sushi[left]] == 0:
            del eat[sushi[left]]
        result = max(result, len(eat))
        left += 1
print(result)
