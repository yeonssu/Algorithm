from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    mid = (sum1 + sum2) / 2
    answer = 0

    n = 3*(len(queue1)-1)
    while sum1 != mid:
        if sum1 > mid:
            a = queue1.popleft()
            sum1 -= a
            queue2.append(a)
        elif sum1 < mid:
            a = queue2.popleft()
            sum1 += a
            queue1.append(a)
    
        answer += 1
        if answer > n:   
            answer = -1
            break

    print(answer)

    return answer

solution([3,2,7,2],[4,6,5,1])
solution([1,2,1,2,],[1,10,1,2])
solution([1,1],[1,5])