import sys
from itertools import combinations

input = sys.stdin.readline
T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    students = list(map(str, input().strip().split()))
    if N > 32:
        print(0)
    else:
        result = 987654321
        for combis in combinations(students, 3):
            score = 0
            for combi in combinations(list(combis), 2):
                A = combi[0]
                B = combi[1]
                for i in range(4):
                    if A[i] != B[i]:
                        score += 1
            result = min(result, score)
        print(result)
