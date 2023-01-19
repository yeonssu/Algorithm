def fib_dp(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib_array = [0, 1]
        
        for i in range(2,n+1):
            print(fib_array[i-1])
            print(fib_array[i-2])
            num = fib_array[i-1] + fib_array[i-2]
            fib_array.append(num)
        return fib_array[n]


T = int(input())
for t in range(T):
    N = int(input())
    fib_dp(N)
