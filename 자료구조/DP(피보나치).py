# 피보나치(fibonacci)수열 - 재귀호출
def fib_naive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib = fib_naive(n-1) + fib_naive(n-2)
        return fib
print(fib_naive(7))

fib_array = [0, 1]
def fib_recur_dp(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
        fib_array.append(fib)
        return fib
print(fib_recur_dp(7))

# 피보나치(fibonacci)수열 - 동적프로그래밍
def fib_dp(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib_array = [0, 1]
        
        for i in range(2,n+1):
            num = fib_array[i-1] + fib_array[i-2]
            fib_array.append(num)
        return fib_array[n]

print(fib_dp(7))
