import sys
from collections import defaultdict

input = sys.stdin.readline
# 우선 순위
# 1. 자주 나오는 단어 일수록
# 2. 단어의 길이가 길수록
# 3. 알파벳 사전 순으로 앞에 있는 단어 일수록
N, M = map(int, input().strip().split())
voca_book = defaultdict(int)
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        voca_book[word] += 1

words_list = sorted(voca_book.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for x in words_list:
    print(x[0])
