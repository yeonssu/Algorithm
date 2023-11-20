import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    people = [list(map(int, input().strip().split())) for _ in range(n)]
    for i, person in enumerate(people):
        score = 1
        for j, another in enumerate(people):
            if i != j and person[0] < another[0] and person[1] < another[1]:
                score += 1
        print(score, end=" ")
