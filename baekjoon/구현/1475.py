import sys, math
input = sys.stdin.readline


if __name__ == "__main__":
    room = list(map(int, input().strip()))
    numbers = [0] * 10
    for r in room:
        numbers[r] += 1
    numbers[6] = math.ceil((numbers[6] + numbers[9]) / 2)
    numbers[9] = 0
    print(max(numbers))
