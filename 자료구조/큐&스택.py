# Stack
def push(data, n):   # data: 스택 리스트, n: 추가할 값
    data.append(n)

def pop(data):       # data: 스택 리스트 
    if len(data)>0:       # 빈 스택을 pop()하면 인덱스 에러 발생
        return data.pop()   # pop함수의 괄호를 비어놓으면 마지막을 빼는 것
    else:
        return False          # 빈 스택이면 False 반환 

stack = []
print('스택:', stack)
for i in range(1,4):
    push(stack, i)
    print('스택:', stack)
for i in range(1,4):
    pop(stack)
    print('스택:', stack)      




# Queue
def enqueue(data, n):
    data.append(n)

def dequeue(data):
    if len(data)>0:        # 빈 큐는 False 반환 
        return data.pop(0)   # 처음 값 빼내서 반환 
    else:
        return False

queue = []
print(' 큐 :', queue)
for i in range(1,4):
    enqueue(queue, i)
    print(' 큐 :', queue)
for i in range(1,4):
    dequeue(queue)
    print(' 큐 :', queue) 
