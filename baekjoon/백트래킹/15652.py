import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().strip().split())
for combi in combinations_with_replacement(range(1, N + 1), M):
    print(*combi)
