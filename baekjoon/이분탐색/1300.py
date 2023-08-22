import sys
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())
lower, upper = 1, K

answer = 0
while lower <= upper:
    middle = (lower + upper) // 2
    cnt = 0
    # N 보다 작은 자연수 곱이 몇 개인지 알아야 한다
    for i in range(1, N + 1):
        cnt += min(middle // i, N)

    if cnt >= K:
        answer = middle
        upper = middle - 1
    else:
        lower = middle + 1
print(answer)
