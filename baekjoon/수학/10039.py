import sys
input = sys.stdin.readline


if __name__ == "__main__":
    scores = 0
    for _ in range(5):
        score = int(input().strip())
        if score <= 40:
            score = 40
        scores += score
    print(scores // 5)
