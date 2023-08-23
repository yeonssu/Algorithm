# 당연히 시간 초과
import sys
from itertools import permutations
input = sys.stdin.readline

num = list(map(int, input().strip()))

answer = -1
for combi in permutations(num, len(num)):
    n = ""
    for c in combi:
        n += str(c)
    n = int(n)
    if n % 30 == 0:
        answer = max(answer, n)

print(answer)
