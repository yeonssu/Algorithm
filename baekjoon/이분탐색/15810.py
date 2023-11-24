import sys
input = sys.stdin.readline


def binary_search(left, right):
    result = 0
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        for time in times:
            cnt += mid // time

        if cnt >= m:
            result = mid
            right = mid - 1
        elif cnt < m:
            left = mid + 1

    return result


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    times = list(map(int, input().strip().split()))
    print(binary_search(0, max(times) * m))
