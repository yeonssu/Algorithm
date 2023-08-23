import sys
input = sys.stdin.readline

num = list(map(int, input().strip()))
num.sort(reverse=True)

answer = -1
if num[len(num) - 1] == 0:
    if sum(num) % 3 == 0:
        answer = "".join(map(str, num))

print(answer)
