# 리스트 : 순서를 가지는 객체의 집합
# 위치찾기index() 추가append() 특정위치에추가insert() 제거pop()
# 개수세기count() 정렬sort() 순서뒤집기reverse()
# 리스트확장(두개를섞음)extend() 모두지우기clear()

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list2 = [5,2,4,3,1]
num_list2.reverse()
print(num_list2)

num_list.extend(num_list2)
print(num_list)

mix_list = [10, "가나다", True] # 숫자형 문자열 Boolean형 모두 가능
print(mix_list)
mix_list.clear()
print(mix_list)


