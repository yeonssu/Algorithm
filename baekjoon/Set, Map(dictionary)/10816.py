import sys
from collections import defaultdict
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    sanggeun = list(map(int, input().strip().split()))
    m = int(input())
    cards = list(map(int, input().strip().split()))
    counts = defaultdict(int)
    for card in sanggeun:
        counts[card] += 1

    for card in cards:
        answer = counts.get(card)
        if answer is None:
            answer = 0
        print(answer, end=" ")

