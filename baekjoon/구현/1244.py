import sys


def turn_on_off(switch, idx):
    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0


def man(switch, num, switch_num):
    idx = num
    i = 1
    while idx <= switch_num:
        idx = num * i
        if idx > switch_num:
            break
        turn_on_off(switch, idx)
        i += 1


def woman(switch, num, switch_num):
    idx = num
    turn_on_off(switch, idx)
    i = 1
    while True:
        idx_right = num + i
        idx_left = num - i
        if idx_right > switch_num or idx_left < 1:
            break
        if switch[idx_right] == switch[idx_left]:
            turn_on_off(switch, idx_right)
            turn_on_off(switch, idx_left)
        else:
            break
        i += 1


input = sys.stdin.readline

switch_num = int(input().strip())
switch = [0]
for s in list(map(int, input().strip().split())):
    switch.append(s)

student_num = int(input().strip())
for _ in range(student_num):
    gender, num = map(int, input().strip().split())
    if gender == 1:  # 남자
        man(switch, num, switch_num)
    else:  # 여자
        woman(switch, num, switch_num)

switch = switch[1:]
for i in range(0, switch_num, 20):
    print(*switch[i:i + 20])

