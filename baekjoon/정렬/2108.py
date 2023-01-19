import sys
from collections import Counter

N = int(input())
num_list = []
for n in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list = sorted(num_list)

#산술평균
print(round(sum(num_list)/N))
#중앙값
print(num_list[N//2])
#최빈값
count = Counter(num_list)

max_count = Counter(num_list).most_common()

if len(max_count)>1 and max_count[0][1]==max_count[1][1]: 
    print(max_count[1][0])
else: 
    print(max_count[0][0])

#범위
print(num_list[len(num_list)-1] - num_list[0])