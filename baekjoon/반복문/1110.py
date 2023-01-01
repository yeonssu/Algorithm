a = int(input())
cnt = 0
num = a

while True:
    num1 = num// 10
    num2 = num % 10
    num3 = num1 + num2
    num3 %= 10
    num = num2*10 + num3
    if a == num:
        break
    cnt += 1
    
print(cnt+1)
