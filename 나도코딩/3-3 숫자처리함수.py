# 숫자처리함수
# 절대값abs() 거듭제곱pow(,) 최댓값max() 최솟값min() 반올림round(,)

print(abs(-5))
print(pow(4,3))
print(max(5,12,24))
print(min(5,12,24))
print(round(3.14159)) # 정수로 반올림
print(round(3.14159, 2)) # 소숫점 둘째자리까지 반올림

# 라이브러리사용(외장함수)
# 내림floor() 올림ceil() 제곱근sqrt()

from math import * # math 라이브러리함수를 가져온다

print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))
