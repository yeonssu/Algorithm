import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    nums = [0] * 10001
    for _ in range(n):
        nums[int(input().strip())] += 1
    for idx, num in enumerate(nums):
        if num != 0:
            for _ in range(num):
                print(idx)
