import sys, math
input = sys.stdin.readline

M, N = map(int, input().strip().split())
for n in range(M, N + 1):
    if n == 1:
        continue

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            break
    else:
        print(n)
