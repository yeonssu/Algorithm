import sys
input = sys.stdin.readline


def find_min_value_index(array):
    min_value = min(array)
    for i, a in enumerate(array):
        if a == min_value:
            return i


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().strip().split())
        a_arr = list(map(int, input().strip().split()))
        b_arr = list(map(int, input().strip().split()))
        b_arr.sort()
        c_arr = 0
        # A = [20, 5, 14, 9] 그리고 B = [8, 12, 16]
        for target in a_arr:
            start, end = 0, m - 1
            while start < end:
                middle = (start + end) // 2
                if b_arr[middle] < target:
                    start = middle + 1
                elif b_arr[middle] > target:
                    end = middle - 1
                elif b_arr[middle] == target:
                    end = middle
            sub = [abs(b_arr[end - 1] - target), abs(b_arr[end] - target), abs(b_arr[(end + 1) % m] - target)]
            idx = find_min_value_index(sub)
            c_arr += b_arr[end + idx - 1]
        print(c_arr)
