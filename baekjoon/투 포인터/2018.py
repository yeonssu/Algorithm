import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    start, end, partial_sum, cnt = 1, 1, 1, 1
    if n == 1 or n == 2:
        print(1)
        exit()

    while end < n:
        if partial_sum < n:
            end += 1
            partial_sum += end
        elif partial_sum > n:
            partial_sum -= start
            start += 1
        elif partial_sum == n:
            cnt += 1
            end += 1
            partial_sum += end
    print(cnt)
