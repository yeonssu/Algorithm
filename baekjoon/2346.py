import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    i = 0
    while nums.count(0) != n:
        print(i, end = " ")
        move = nums[i]
        nums[i] = 0
        # 움직여야하는 칸이 양수라면
        if move > 0:
            j = 1
            while j != move:
                if nums[(i + j) % n] != 0:
                    j += 1
        # 움직여야하는 칸이 음수라면
        else:
            move *= -1
            j = 1
            while j != move:
                if nums[(i + j) % n] != 0:
                    j += 1
        print(j)
        i = j
    