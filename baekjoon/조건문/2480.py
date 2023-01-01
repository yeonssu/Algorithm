a, b, c = map(int, input().split())

if a==b and b==c:
    print(10000+1000*a)
elif a==b or a==c:
    print(1000+100*a)
elif b==c:
    print(1000+100*b)
else:
    d = max(a,b,c)
    print(d*100)