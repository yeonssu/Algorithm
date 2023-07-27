import sys
input = sys.stdin.readline

N = int(input().strip())
number = [int(input().strip()) for _ in range(N)]
for n in sorted(number):
    print(n)
