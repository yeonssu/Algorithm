def linear_search(array, search_value):
    for i in range(len(array)):
        if search_value == array[i]:
            return i
    return None

print(linear_search([2, 3, 5, 7, 11],2))
print(linear_search([2, 3, 5, 7, 11],0))
print(linear_search([2, 3, 5, 7, 11],5))
print(linear_search([2, 3, 5, 7, 11],3))
print(linear_search([2, 3, 5, 7, 11],11))