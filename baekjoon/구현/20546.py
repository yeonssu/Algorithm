import sys
input = sys.stdin.readline


if __name__ == "__main__":
    cash = int(input().strip())
    cash_jun = cash
    cash_sung = cash
    machine_duck = list(map(int, input().strip().split()))
    # 준현 : 주식을 살 수 있다면 무조건 최대한 많이 산다
    # 성민 : 전량 매수, 3일동안 상승 -> 전량 매도, 3일동안 하락 -> 전량 매수
    jun = [0] * 14
    sung = [0] * 14
    for day in range(14):
        stock = machine_duck[day]
        if cash_jun >= stock:
            jun[day] = cash_jun // stock
            cash_jun -= stock * jun[day]

        if day - 3 >= 0 and machine_duck[day - 3] < machine_duck[day - 2] < machine_duck[day - 1] < machine_duck[day]:
            if sum(sung) > 0:
                cash_sung += sum(sung) * machine_duck[day]
                sung = [0] * 14
        elif day - 3 >= 0 and machine_duck[day - 3] > machine_duck[day - 2] > machine_duck[day - 1] > machine_duck[day]:
            if cash_sung >= stock:
                sung[day] = cash_sung // stock
                cash_sung -= stock * sung[day]

    total_jun = cash_jun + machine_duck[-1] * sum(jun)
    total_sung = cash_sung + machine_duck[-1] * sum(sung)
    if total_jun > total_sung:
        print("BNP")
    elif total_jun < total_sung:
        print("TIMING")
    else:
        print("SAMESAME")
