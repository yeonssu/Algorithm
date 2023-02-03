# 오답
import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
record_length = list(map(int, input().split()))

lower = max(record_length)
upper = sum(record_length)
result = 100000

while lower <= upper:
    mid = (lower + upper) // 2
    # print("===========")
    # print("mid", mid)

    cnt = 1
    sub_blu_ray = 0
    for i in range(N):
        if sub_blu_ray + record_length[i] > mid:  # 넣을 수 없는 경우
            cnt += 1
            sub_blu_ray = 0
        sub_blu_ray += record_length[i]
        # print(sub_blu_ray)
        # print("cnt",cnt)

    if cnt <= M:
        if cnt == M:
            result = min(result, mid)
        upper = mid - 1
    elif cnt > M:
        lower = mid + 1

print(result)
