import math

def solution(n, k):
    fullnumber = []

    while n >= k :
        fullnumber.append(n%k)
        n = n//k
        if n<k :
            fullnumber.append(n)

    fullnumber = ''.join(map(str, fullnumber[::-1]))

    split_list = fullnumber.split("0")
    print(split_list)
    
    answer = 0
    for n in split_list:
        if len(n)== 0:
            answer = answer
        elif int(n) == 1 or int(n) == 0:
            answer = answer
        else:
            if primenumber(int(n)) == True:
                answer += 1
    print(answer)
    return answer

def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
    # return True

solution(437674,3)
solution(110011,10)