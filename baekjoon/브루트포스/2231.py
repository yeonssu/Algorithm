N = int(input())
result=[]

for i in range(1,N+1):
    string_i = str(i)
    each_value = list(string_i)
    each_value_int = []
    for j in each_value:
        each_value_int.append(int(j))

    total = sum(each_value_int) + i
    if(total==N):
        result.append(i)

if len(result)==0:
    print(0)
else:
    print(min(result))