N = int(input())
N_list = list(map(int,input().split()))
N_list = sorted(N_list)

M = int(input())
M_list = list(map(int,input().split()))

def binary_search(array, search_value):

    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2

        value_at_midpoint = array[midpoint]

        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1

for m in M_list :
    if (binary_search(N_list,m)==None):
        print(0)
    else:
        print(1)