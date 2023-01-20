def push(data, n):   # data: 스택 리스트, n: 추가할 값
    data.append(n)
def pop(data):       # data: 스택 리스트 
    if len(data)>0:       # 빈 스택을 pop()하면 인덱스 에러 발생
        return data.pop()   # pop함수의 괄호를 비어놓으면 마지막을 빼는 것
    else:
        return False          # 빈 스택이면 False 반환 


while True:
    
    input_value = input()
    if input_value==".":
        break

    stack = []
    for i in input_value:
        if i=="(" or i=="[":
            push(stack,i)
        if i==")" or i=="]":
            if len(stack)==0:
                push(stack,i)
                break
#             elif stack.
#                 pop(stack)
            
# print("yes")

#     print(stack)