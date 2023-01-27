N, M = map(int, input().split())

tree = list(map(int, input().split()))

short = 1
long = max(tree)

while short <= long:
    mid = (long+short)//2

    collect = 0
    for t in tree:    
        if t > mid : collect += (t-mid)

    # 모은 길이가 목표치보다 크면 최소값을 mid값으로 바꾸고 다시 실행
    if collect >= M : short = mid+1
    # 모은 길이가 목표치보다 작으면 최대값을 mid값으로 바꾸고 다시 실행
    if collect < M : long = mid-1
print(long)




''' 이거 왜 안돼?
    # 모은 길이가 목표치와 같으면 출력하고 끝내기
    if collect == M :
        print(mid)
        break
    # 모은 길이가 목표치보다 크면 최소값을 mid값으로 바꾸고 다시 실행
    if collect > M : short = mid+1
    # 모은 길이가 목표치보다 작으면 최대값을 mid값으로 바꾸고 다시 실행
    if collect < M : long = mid-1
    
'''