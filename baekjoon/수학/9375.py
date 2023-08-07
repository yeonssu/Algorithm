import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    clothes = defaultdict(int)
    n = int(input().strip())
    for _ in range(n):
        name, kind = map(str, input().strip().split())
        clothes[kind] += 1
    answer = 1
    for kind in clothes.keys():
        answer *= (clothes.get(kind) + 1)
    print(answer - 1)
