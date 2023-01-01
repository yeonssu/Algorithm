wine_list = []
result_list = [0]*10000

n = int(input())
for i in range(n):
    wine = int(input())
    wine_list.append(wine)

if n == 1 :
    result_list[0] = wine_list[0]
elif n == 2:
    result_list[0] = wine_list[0]
    result_list[1] = wine_list[0] + wine_list[1]
else:
    result_list[0] = wine_list[0]
    result_list[1] = wine_list[0] + wine_list[1]
    result_list[2] = max(wine_list[1]+wine_list[2], wine_list[0]+wine_list[2], wine_list[0]+wine_list[1])
    for i in range(3,n):
        result_list[i] = max(result_list[i-3] + wine_list[i-1] + wine_list[i], result_list[i-2]+ wine_list[i], result_list[i-1])

print(result_list[n-1])
