def count_zero(n):
    cnt = 0
    while n >= 5:
        cnt += n // 5
        n = n // 5
    return cnt


M = int(input())
lower = 1
upper = M * 5
result = 100000000

while lower <= upper:
    mid = (lower + upper) // 2

    zero = count_zero(mid)
    # print("upper", upper, "lower", lower, "mid", mid)
    # print("zero", zero)
    if zero < M:
        lower = mid + 1
    elif zero >= M:
        if zero == M:
            result = mid
        upper = mid - 1

if result == 100000000:
    print(-1)
else:
    print(result)
