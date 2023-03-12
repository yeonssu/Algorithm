# 메모리 초과
import sys, itertools

input = sys.stdin.readline

N = int(input().strip())
number = list(range(1, N + 1))
nPr = list(itertools.permutations(number, N))

nPr.sort()
want_value = tuple(map(int, input().strip().split()))
for i in range(len(nPr)):
    if nPr[i] == want_value:
        if i - 1 < 0:
            print(-1)
        else:
            print(*nPr[i - 1])
