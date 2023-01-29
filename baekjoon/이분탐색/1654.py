K, N = map(int, input().split())
wires = [ int(input()) for _ in range(K)]

short_len = 1
long_len = max(wires)

while short_len <= long_len:
        midlen = (short_len + long_len) // 2

        count = 0
        for wire in wires:
            count += wire//midlen
        #print(long_len, short_len, midlen, count)

        # 모은 개수가 목표N보다 작으면 길이를 내려야함(long 값을 줄여야함)
        if count < N:
            long_len = midlen - 1
        # 모은 개수가 목표N보다 크면 숫자를 올려야함(short 값을 키워야함)
        # 모은 개수가 목표N과 같을 떄는 여기에 포함
        # 최대랜선의 길이를 구해야하므로 값이 나왔더라도 숫자를 올려 위값에 만족하는 것이 있는지 확인해야한다
        elif count >= N:
            short_len = midlen + 1

print(long_len)