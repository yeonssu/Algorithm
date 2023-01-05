# N = int(input())
# input_list = list(map(int,input().split()))
import sys
N = int(sys.stdin.readline())
input_list = list(map(int,sys.stdin.readline().split(" ")))


result = []

def thtn(a):
    if a==1:
        return False
    elif a==2:
        return True
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True

for value in input_list:
    if(thtn(value)): result.append(value)

print(len(result))

