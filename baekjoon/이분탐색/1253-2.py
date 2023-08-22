import sys
input = sys.stdin.readline

# binary search처럼 middle값으로 하면 틀리고
# 투포인터처럼 하면 +=1 -=1 하면 맞는다 -> 왜그럴까? ㅜㅜ
def binary_search(array, search_value):
    global answer
    lower = 0
    upper = len(array) - 1

    while lower < upper:
        sum_value = array[lower] + array[upper]

        if sum_value == search_value:
            answer += 1
            break
        elif sum_value < search_value:
            lower += 1
        elif sum_value > search_value:
            upper -= 1


N = int(input().strip())
A = list(map(int, input().strip().split()))
A = sorted(A)
answer = 0
# 2부터 N 까지만 해도 된다고 생각 했으나 틀렸다
# for i in range(2, N):
# 왜 틀렸지? A 배열에 음수가 주어질 수도 있네? 그럼 앞 두 개를 빼면 안되지 !
for i in range(2, N):
    temp = A[:i] + A[i + 1:]
    binary_search(temp, A[i])

print(answer)

'''
1 2 3 4 5 6 7 8 9 10

i = 1
2345678910

i = 2
1345678910
'''