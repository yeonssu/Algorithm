import sys
input = sys.stdin.readline

L, C = map(int, input().strip().split())

# 암호 조건
# 1. 최소 한 개의 모음, 최소 두 개의 자음
# 2. 정렬된 문자열
# L : 암호 길이 / C : 문자 종류

chars = list(map(str, input().strip().split()))
chars = sorted(chars)


def solve(index, moeum, jaeum, result):
    if len(result) == L and moeum >= 1 and jaeum >= 2:
        print(result)
        return
    for i in range(index, C):
        if chars[i] == "a" or chars[i] == "e" or chars[i] == "i" or chars[i] == "o" or chars[i] == "u":
            solve(i + 1, moeum + 1, jaeum, result + chars[i])
        else:
            solve(i + 1, moeum, jaeum + 1, result + chars[i])


solve(0, 0, 0, "")
