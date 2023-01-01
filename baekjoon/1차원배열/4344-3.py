n = int(input())
scores = []
count = 0

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

for i in range(n):
    N, *scores = map(int, input().split())
    ave = average(N, scores)
    count1 = percent(count,ave)
    rate = (count1/N)*100
    print(f'{rate:.3f}%')
