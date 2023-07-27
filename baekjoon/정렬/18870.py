import sys
input = sys.stdin.readline

N = int(input().strip())
number = list(map(int, input().strip().split()))
sorted_number = sorted(set(number))

for n in number:
    print(sorted_number.index(n), end=" ")
