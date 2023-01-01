# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("생년 : " + jumin[0:2])
print("월일 : " + jumin[2:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 마지막까지
print("뒤 7자리(역순) : " + jumin[-7:]) # 음수값은 맨 뒤에서부터의 위치
