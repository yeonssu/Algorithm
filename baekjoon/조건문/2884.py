H, M = map(int, input().split())
M -= 45
if M < 0:
    if H == 0 :
        H = 23
    else:
        H -= 1
    print(H,M+60)
else:
    print(H,M)

# 줄일 수 있는 방법 없을까?
hour, minute = map(int, input().split())

ALARM_TIME = 45

minute = minute - ALARM_TIME

if minute < 0:
    minute += 60
    hour -= 1

if hour < 0:
    hour += 24

print(hour, minute)