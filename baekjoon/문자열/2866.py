import sys
from collections import deque, Counter

input = sys.stdin.readline
R, C = map(int, input().strip().split())

arr = [deque() for _ in range(C)]
cnt = 0
for i in range(R):
    a = input().strip()
    for j in range(C):
        arr[j].append(a[j])

cnt = 0
for j in range(R-1):
    for i in arr:
        i.popleft()

    word = []
    for i in arr:
        word.append("".join(i))
    counter = Counter(word)
    print(counter)
    if list(dict(counter).values()).count(1) == C:
        cnt += 1
    else:
        break

print(cnt)
