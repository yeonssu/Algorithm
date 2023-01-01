num = int(input())

# for i in range(num):
#     print(" "*(num-i-1) ,"*"*(i+1))
    
for i in range(num):
    star = (i+1)*"*"
    print(star.rjust(num))