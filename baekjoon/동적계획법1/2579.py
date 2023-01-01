score_list = []
result_list = [0]*300

n = int(input())
for i in range(n):
    score = int(input())
    score_list.append(score)
if n == 1 :
    result_list[0] = score_list[0]
elif n == 2:
    result_list[0] = score_list[0]
    result_list[1] = score_list[0] + score_list[1]
else:
    result_list[0] = score_list[0]
    result_list[1] = score_list[0] + score_list[1]
    result_list[2] = max(score_list[1]+score_list[2], score_list[0]+score_list[2])
    for i in range(3,n):
        result_list[i] = max(result_list[i-3] + score_list[i-1] + score_list[i], result_list[i-2]+ score_list[i])


print(result_list[n-1])
