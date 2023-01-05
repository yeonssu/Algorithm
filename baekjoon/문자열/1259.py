finish = 1
input_list = []
while(finish!=0):
    input_value = int(input())
    input_list.append(input_value)
    finish = input_value

input_list.remove(0)

for i in input_list:
    value = str(i)
    midlepoint = len(value)//2
    first = value[:midlepoint]

    if(len(value)%2==0):
        second = value[midlepoint:]
    else:
        second = value[midlepoint+1:]
    
    second = second[::-1]
    if(first==second):
        print("yes")
    else:
        print("no")
