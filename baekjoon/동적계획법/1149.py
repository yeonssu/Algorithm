import sys
input = sys.stdin.readline

N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().strip().split())))

for i in range(1, N):
    # 이전 집 중, 같은 색을 제외한 색의 비용 중 작은 것을 계속 더한다
    RGB[i][0] += min(RGB[i - 1][1], RGB[i - 1][2])
    RGB[i][1] += min(RGB[i - 1][0], RGB[i - 1][2])
    RGB[i][2] += min(RGB[i - 1][0], RGB[i - 1][1])
print(min(RGB[N - 1]))
