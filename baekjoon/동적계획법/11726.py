# n=1이면 | 1가지
# n=2이면 =, || 2가지
# n=3이면 |=, =|, ||| 3가지
# n=4이면 ==, ||=, |=|, =||, |||| 5가지
# n=5이면 ==|, =|=, |==,  |||=, ||=|, |=||, =|||, ||||| 8가지
# 어? 피보나치네? 근데 왜 피보나치처럼 되는거지? 

n = int(input())

def fib(n):
    if n==1 : result = 1
    elif n==2 : result = 2
    else : 
        fibbo = [0,1,2]
        for i in range(3,n+1):
            fibbo.append(fibbo[i-1] + fibbo[i-2])
        
        result = fibbo[n]

    return result

print(fib(n)%10007)