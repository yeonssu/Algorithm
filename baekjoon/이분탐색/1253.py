import sys
input = sys.stdin.readline


def binary_search(array, search_value):
    global answer
    lower = 0
    upper = len(array) - 1

    while lower < upper:
        sum_value = array[lower] + array[upper]
        middle = (lower + upper) // 2

        if sum_value == search_value:
            answer += 1
            break
        elif sum_value < search_value:
            lower = middle + 1
        elif sum_value > search_value:
            upper = middle - 1


N = int(input().strip())
A = list(map(int, input().strip().split()))
A = sorted(A)
answer = 0
for i in range(N):
    temp = A[:i] + A[i + 1:]
    binary_search(temp, A[i])

print(answer)
