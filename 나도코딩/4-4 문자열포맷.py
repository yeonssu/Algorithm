# 문자열포맷
print("a"+"b")
print("a","b")

# 방법1 : %d정수 %s문자열 %c문자
print("나는 %d살입니다." %20)
print("Apple은 %c로 시작해요." %"A")
print("나는 %s을 좋아해요." %"파이썬")
print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

# 방법2 : 포맷함수format()
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))

# 방법3 : 설정한변수이용 문자열앞에f를 적는다
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")