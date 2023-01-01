# 문자열처리함수

# 소문자lower() 대문자upper() 소문자판별islower() 대문자판별isupper()
# 길이len() 교환replace(,) 문자개수count()
python = "Python is Amazing"

print(python.lower())  
print(python.upper())
print(python[0].islower())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
print(python.count("n"))

# 문자위치찾기find() index()  (find는 원하는 값이 없으면 -1반환 index는 오류)
print(python.find("n"))
index = python.index("n")   # 첫번째 n의 위치
print(index)
index = python.index("n", index + 1) # 그다음 n의 위치
print(index)
