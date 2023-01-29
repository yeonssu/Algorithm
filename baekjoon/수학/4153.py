while True:
    # 만약 abc가 큰 순서로 주어지면
    # a, b, c = map(int, input().split())
    # if a==0 and b==0 and c==0 : break

    # if c*c == a*a + b*b : print("right")
    # else: print("wrong")
    num = list(map(int,input().split()))
    if sum(num)==0: break

    max_value = max(num)
    num.remove(max_value)

    if max_value*max_value == num[0]*num[0] + num[1]*num[1]:
        print("right")
    else:
        print("wrong")
