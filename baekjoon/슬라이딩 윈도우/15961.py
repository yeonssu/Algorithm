import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().strip().split())
sushi = []
for n in range(N):
    sushi.append(int(input().strip()))
sushi.extend(sushi)
print(sushi)
# 쿠폰에 있는 건 무조건 먹기
eat = defaultdict(int)
eat[c] = 1

# k개씩 잘라가면서 먹은 거의 갯수 증가시키고 감소시키기
result = 0
left = 0
for right in range(len(sushi)):
    eat[sushi[right]] += 1

    if right >= k - 1:
        result = max(result, len(eat))
        eat[sushi[left]] -= 1
        if eat[sushi[left]] == 0:
            del eat[sushi[left]]
        left += 1

print(result)

# 입력값 : 7, 9, 7, 30, 2, 7, 9, 25
# sushi : 7, 9, 7, 30, 2, 7, 9, 25, 7, 9, 7, 30, 2, 7, 9, 25
# eat : 일단 쿠폰에 있는거 먹기 {30:1개}
# 첫 번째 루프 : 7,9,7,30 먹겠지 -> {7:2개, 30:2개, 9:1개} -> 3종류
# 두 번째 루프 : 9,7,30,2 먹겠지 -> 7을 안먹고 2를 먹었다고 한다 -> {7:1개, 30:2개, 9:1개, 2:1개} -> 4종류
# 세 번째 루프 : 7,30,2,7 먹겠지 -> 9를 안먹고 7을 먹었다고 한다 -> {7:2개, 30:2개, 9:0개, 2:1개} -> {7:2개, 30:2개, 2:1개} -> 3종류
# 네 번째 루프 : 30,2,7,9 먹겠지 -> 7를 안먹고 9을 먹었다고 한다 -> {7:1개, 30:2개, 9:1개, 2:1개} -> 4종류
# 다섯 번째 루프 : 2,7,9,25 먹겠지 -> 30를 안먹고 25을 먹었다고 한다 -> {7:1개, 30:1개, 9:1개, 2:1개, 25:1개} -> 5종류 <<정답>>
