'''
5! = 120 = 2^3 * 3 * 5 -> 0 개수 1개
...
10! = 3628800 = 2^8 * 3^4 * 5^2 * 7 -> 0 개수 2개
...
15! = 1307674368000 = 2^11 * 3^6 * 5^3 * ... -> 0 개수 3개
...
20! = 2432902008176640000 = 2^18 * 3^8 * 5^4 ... -> 0의 개수 4개
...
25! = 15511210043330985984000000 = 2^22 * 3^10 * 5^6 ... -> 0의 개수 6개
...
30! = 265252859812191058636308480000000
    = 2^26 * 3^14 * 5^7 ... -> 0의 개수 7개
-> 소인수분해 했을 때 5의 개수가 즉 10의 개수
'''


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
