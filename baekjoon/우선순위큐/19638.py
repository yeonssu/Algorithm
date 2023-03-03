import sys, heapq

input = sys.stdin.readline

N, H, T = map(int, input().strip().split())
height = []
for n in range(N):
    heapq.heappush(height, -int(input().strip()))

cnt = 0
for t in range(T):
    # 뿅망치 적용 전, 탈출 조건 실행 x
    tallest_height = -heapq.heappop(height)
    if H > tallest_height:
        print("YES")
        print(cnt)
        exit()

    # 뿅망치 적용 (1이면 적용 x, 1이 아니면 적용)
    if tallest_height == 1:
        heapq.heappush(height, -tallest_height)
        cnt += 1
    else:
        changed_height = tallest_height // 2
        heapq.heappush(height, -changed_height)
        cnt += 1

    # 뿅망치 적용 이후, 가장 큰 값이 센티보다 작으면 종료, 센티보다 크면 계속 실행
    tallest_height = -height[0]
    if H > tallest_height:
        print("YES")
        print(cnt)
        exit()

print("NO")
print(-heapq.heappop(height))
