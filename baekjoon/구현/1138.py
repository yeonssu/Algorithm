import sys
input = sys.stdin.readline

N = int(input().strip())
heights = list(map(int, input().strip().split()))
answer = [0 for _ in range(N)]

for i in range(N):
    left_taller_count = heights[i]
    cnt = 0
    for j in range(N):
        if cnt == left_taller_count:
            if answer[j] == 0:
                answer[j] = i + 1
                break
        else:
            if answer[j] == 0:
                cnt += 1

print(*answer)
