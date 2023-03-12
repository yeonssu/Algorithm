import sys

input = sys.stdin.readline

# 종이가로길이 W, 종이세로길이 H, 세로로 접는 곳 f, 가로로 나눌 크기 c
# (x1, y1)와 (x2, y2)를 찾아서 색칠한다
W, H, f, c, x1, y1, x2, y2 = map(int, input().strip().split())

# result = H * W
# paper = 0
# for i in range(H // (c + 1)):
#     for j in range(max(f, W - f)):
#         if j < min(f, W - f):
#             paper = 2 * (c + 1)
#         else:
#             paper = 1 * (c + 1)
#
#         if y1 <= i < y2 and x1 <= j < x2:
#             result -= paper
#
# print(result)


# result = H * W
# paper = 0
# for x in range(x1, x2):
#     if x < min(f, W - f):
#         paper = 2 * (c + 1)
#     else:
#         paper = 1 * (c + 1)
#     result -= paper * (y2 - y1)
#
# print(result)


result = H * W
a = min(f, W-f)
if x2 <= a:
    result -= 2 * (c + 1) * (x2 - x1) * (y2 - y1)
if x1 < a < x2:
    result -= 2 * (c + 1) * (min(f, W - f) - x1) * (y2 - y1)
    result -= 1 * (c + 1) * (x2 - min(f, W - f)) * (y2 - y1)
if x1 >= a:
    result -= 1 * (c + 1) * (x2 - x1) * (y2 - y1)
print(result)

