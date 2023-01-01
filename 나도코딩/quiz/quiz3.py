# (Quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2 : 처음 만나는 점(.)이후 부분은 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e'갯수 + "!"로 구성

# 생성된 비밀번호 : nav51!

# 풀이
address = "http://youtube.com"
rule1 = address[7:]
rule2 = rule1[:rule1.index(".")]
rule3 = rule2[:3]

print(rule3 + str(len(rule2)) + str(rule2.count("e")) +"!")

# 답
url = "http://youtube.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(password)