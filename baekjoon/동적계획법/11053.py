import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))

answer = 0
for n in range(1, N + 1):
    for combi in combinations(A, n):
        combi_list = list(combi)
        for i in range(len(combi_list) - 1):
            if combi_list[i] >= combi_list[i + 1]:
                break
            else:
                if i == len(combi_list) - 2:
                    answer = max(answer, len(combi_list))

print(answer)
