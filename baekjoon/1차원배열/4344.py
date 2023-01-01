# 입력을 받는다 학생수, 그에 따른 점수

# 평균내는 함수

# 그 함수를 넘어가면 카운트 안넘어가면 X
# 카운트를 백분율로 환산 하고
# round셋째자리


# test_case = int(input())
# for i in range(test_case):
#     N, *scores = input().split()
scores = []
count = 0
N, *scores = map(int, input().split())

def average(N, scores):
    total = sum(scores)
    ave = total / N
    return ave

def percent(count,ave):
    for score in scores:
        if score > ave:
            count += 1
        else:
            continue
    return count    
    
ave = average(N, scores)
count1 = percent(count,ave)
rate = (count1/N)*100
print("{}%".format(round(rate,3)))