import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    people = list(range(1, n + 1))
    answer = "<"
    start = 0
    for length in reversed(range(1, n + 1)):
        finish = start + (k - 1)
        finish %= length
        a = people.pop(finish)
        answer += str(a)
        if length != 1:
            answer += ", "
        start = finish
    answer += ">"
    print(answer)
