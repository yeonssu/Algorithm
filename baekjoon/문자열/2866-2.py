import sys
from collections import deque, Counter

input = sys.stdin.readline
R, C = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(R)]

cnt = 0
lower, upper = 0, R - 1

while lower <= upper:
    mid = (lower + upper) // 2

    words = []
    for i in range(C):
        word = ""
        for j in range(mid, R):
            word += arr[j][i]
        words.append(word)
    counter = Counter(words)

    if list(dict(counter).values()).count(1) == C:
        result = mid
        lower = mid + 1
    else:
        upper = mid - 1

print(result)
