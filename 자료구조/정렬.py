# 버블정렬
def bubble_sort(array):
    num = len(array)
    for i in range(num-1):
        for j in range(num-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return

input = [4, 6, 2, 9, 1]
bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9]



# 선택정렬
def selection_sort(array):
    num = len(array)
    for i in range(num-1):
        min_idx = i
        for j in range(i, num):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i],array[min_idx] = array[min_idx], array[i]
    return

input = [4, 6, 2, 9, 1]
selection_sort(input)
print(input) # [1, 2, 4, 6, 9]



# 삽입정렬
def insertion_sort(array):
    num = len(array)
    for i in range(1,num):
        for j in range(i,0,-1):
            if array[j-1] > array[j]:
                array[j],array[j-1] = array[j-1],array[j]
            else:
                break
    print(array)
    return

input = [4, 6, 2, 9, 1]
insertion_sort(input)
print(input) # [1, 2, 4, 6, 9]