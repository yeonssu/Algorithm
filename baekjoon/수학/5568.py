import sys
from itertools import permutations
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    answer = set()
    for per in permutations(nums, k):
        a = ""
        for p in per:
            a += str(p)
        answer.add(a)
    print(len(answer))
