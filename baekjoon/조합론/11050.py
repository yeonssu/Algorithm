import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    print(len(list(combinations(list(range(n)), k))))