import sys

input = sys.stdin.readline

N = int(input().strip())
sang_geun = list(map(int, input().strip().split()))
sang_geun = sorted(sang_geun)
M = int(input().strip())
cards = list(map(int, input().strip().split()))


def binary_search(array, search_value):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        value_at_midpoint = array[midpoint]

        if search_value == value_at_midpoint:
            return 1
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1
    return 0


result = []
for card in cards:
    result.append(binary_search(sang_geun, card))
print(*result)
