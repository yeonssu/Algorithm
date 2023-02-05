import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())

arr = set()
for n in range(N):
    arr.add(input().strip())

result = 0
for m in range(M):
    s = input().strip()
    if s in arr:
        result += 1

print(result)
