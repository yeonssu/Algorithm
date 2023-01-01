# # 각자리수 합
# n = 1657

# def solution(n):
#     N=[int(i) for i in str(n)]
#     return sum(N)

# a = solution(n)
# print(a)

# # 각 자리수 분리
# n = 1657
# lst = list(map(int, str(n)))
# print(lst)

# def push(data, n):   # data: 스택 리스트, n: 추가할 값

#     data.append(n)


# def pop(data):       # data: 스택 리스트 
#     if len(data)>0:       # 빈 스택을 pop()하면 인덱스 에러 발생

#         return data.pop()
#     return False          # 빈 스택이면 False 반환 

# stack = []
# print('스택:', stack)
# for i in range(1,4):

#     push(stack, i)

#     print('스택:', stack)
# for i in range(1,4):

#     pop(stack)

#     print('스택:', stack) 

# def no_continuous(arr):
#     answer = []
#     for i in arr:
#         if answer[-1:] == [i]:
#             continue
#         else:
#             answer.append(i)
#     return answer

# #기초-출력
# print("Hello")

# print("Hello World")

# print("Hello")
# print("World")

# print("\'Hello\'")

# print("\"Hello\"")

# print("\"!@#$%^&*()\'")

# print("\"C:\Download\\'hello\'.py\"")

# print("print(\"Hello\\nWorld\")")

# #기초-입출력
# a = input()
# print(a)

# a = int(input())
# print(a)

# a = float(input())
# print(a)

# a = int(input())
# b = int(input())
# print(a)
# print(b)

# a = input()
# b = input()
# print(b)
# print(a)

# a = float(input())
# print(a)
# print(a)
# print(a)

# a, b = map(int,input().split())
# print(a)
# print(b)

# a, b = input().split()
# print(b, a)

# a = input()
# print(a, a, a)

