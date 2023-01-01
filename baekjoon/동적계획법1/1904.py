Num = int(input())

result_list = [0]*1000000

result_list[0] = 1
result_list[1] = 2

for i in range(Num-2):
    result_list[i+2] = (result_list[i] + result_list[i+1]) % 15746

print(result_list[Num-1])
