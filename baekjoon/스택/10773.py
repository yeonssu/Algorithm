import sys
input = sys.stdin.readline

num = []
for _ in range(int(input().strip())):
    n = int(input().strip())
    if n == 0:
        num.pop()
    else:
        num.append(n)

print(sum(num))
