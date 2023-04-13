import math
import sys

input = sys.stdin.readline

rh, rv, sh, sv = map(int, input().strip().split())
n = int(input().strip())

answer = 9999999999


def calculate(a, b, c, d, price):
    # 가로
    length = max(math.ceil(rh / a), math.ceil(sh / c))

    # 세로
    width = max(math.ceil(rv / b), math.ceil(sv / d))

    return length * width * price


for i in range(n):
    # 입력받기
    rhi, rvi, shi, svi, pi = map(int, input().strip().split())
    # 회전
    answer = min(answer, calculate(rhi, rvi, shi, svi, pi), calculate(rvi, rhi, svi, shi, pi))

print(answer)
