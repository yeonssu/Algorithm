import sys
input = sys.stdin.readline


def accumulate(li):
    accumulated_sum = [li[0]]
    for i in range(1, len(li)):
        accumulated_sum.append(accumulated_sum[i - 1] + li[i])
    return accumulated_sum


if __name__ == "__main__":
    n = int(input())
    honey = list(map(int, input().strip().split()))
    # 누적합
    acc_sum = accumulate(honey)

    answer = 0
    if n == 3:
        answer = max(honey[0] * 2, honey[1] * 2, honey[2] * 2)

    # 벌통이 제일 왼쪽 일 때 -> 벌통 ... bee1 (... 에 bee2 존재)
    for i in range(1, n - 1):
        bee1 = acc_sum[-1] - honey[-1] - honey[i]
        bee2 = acc_sum[i - 1]
        answer = max(answer, bee1 + bee2)

    # 벌통이 제일 오른쪽 일 때 -> bee1 ... 벌통 (... 에 bee2 존재)
    for i in range(1, n - 1):
        bee1 = acc_sum[-1] - honey[0] - honey[i]
        bee2 = acc_sum[-1] - acc_sum[i]
        answer = max(answer, bee1 + bee2)

    # 벌통이 가운데 일 때 -> bee1 ... bee2 (... 에 벌통 존재)
    for i in range(1, n - 1):
        bee1 = acc_sum[i] - honey[0]
        bee2 = acc_sum[-1] - honey[-1] - acc_sum[i - 1]
        answer = max(answer, bee1 + bee2)

    print(answer)
