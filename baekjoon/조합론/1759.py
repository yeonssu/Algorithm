import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().strip().split())

# 암호 조건
# 1. 최소 한 개의 모음, 최소 두 개의 자음
# 2. 정렬된 문자열
# L : 암호 길이 / C : 문자 종류

chars = list(map(str, input().strip().split()))
chars = sorted(chars)

for combi in combinations(chars, L):
    moeum = 0
    jaeum = 0
    for i in combi:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            moeum += 1
        else:
            jaeum += 1
    if moeum >= 1 and jaeum >= 2:
        print("".join(combi))
