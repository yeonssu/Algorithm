N = int(input())

for i in range(N):
    scores = []
    count = 0
    n, *scores = map(int, input().split())
    total = sum(scores)
    ave = total / n
    for s in scores:
        if s > ave:
            count += 1
    rate = (count/n)*100
    # print(f'{rate:.3f}%')
