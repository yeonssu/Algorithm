a, b = map(int, input().split())
c = int(input())

if b+c >= 60:
    hr = (b+c)//60
    min = (b+c)%60
    if a+hr < 24:
        print(a+hr, min)
    else:
        print(a+hr-24, min)
else:
    if a < 24:
        print(a, b+c)
    else:
        print(a-24, b+c)

# 줄일 수 있는 방법은 없을까?
hour, minute = map(int, input().split())
plus_time = int(input())

plus_time_hour = plus_time // 60
plus_time_minute = plus_time % 60

minute += plus_time_minute
hour += plus_time_hour

if minute >= 60:
    minute = minute - 60
    hour += 1

if hour >= 24:
    hour = hour - 24

print(hour, minute)
