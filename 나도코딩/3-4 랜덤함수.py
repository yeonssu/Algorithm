# 랜덤함수
# 0~1미만값random() a~b미만정수randrange(a,b) a~b이하정수randint(a,b)
from random import * # random 라이브러리함수를 가져온다
print(random())                 # 0.0 ~ 1.0 미만의 임의의 값
print(random() * 10)            # 0.0 ~ 10.0 미만의 임의의 값
print(int(random() * 10))       # 0 ~ 10 미만의 임의의 정수 # int 실수->정수
print(int(random() * 10) + 1)   # 1 ~ 11 미만의 임의의 정수
print(randrange(1, 11))         # 1 ~ 11미만의 임의의 정수
print(randint(1, 10))           # 1 ~ 10이하의 임의의 정수

# 랜덤함수를 이용한 로또값 출력(1~45중 6개)
# random()
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
# randrange(a,b) a ~ b 미만의 임의의 정수
print(randrange(1,46)) 
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
# randint(a,b) a ~ b 이하의 임의의 정수
print(randint(1,45)) 
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))