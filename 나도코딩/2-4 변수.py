# 변수
# 애완동물을 소개해주세요~
print("우리집 강아지의 이름은 연탄이예요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# 같은 문장들을 변수를 설정하여 만들 수 있다
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # str : 숫자를 문자열로 변환
print(name + "는 어른일까요? " + str(is_adult)) # str : Boolean을 문자열로 변환

#  쉼표로도 연결할 수 있다
animal = "고양지"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3
print("우리집 ", animal, "의 이름은 ", name, "예요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")  # 쉼표로 연결하면 str없어도된다
print(name, "는 어른일까요? ", is_adult) 