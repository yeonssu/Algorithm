import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
number = list(map(int, input().strip().split()))
number_dict = defaultdict(int)
sorted_number = sorted(set(number))
for i in range(len(sorted_number)):
    number_dict[sorted_number[i]] = i

for n in number:
    print(number_dict.get(n), end=" ")
