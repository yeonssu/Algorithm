# 시간 초과
def solution(phone_book):
    for i in range(len(phone_book)):
        prefix = phone_book[i]
        copy_book = phone_book[:i] + phone_book[i + 1:]
        for num in copy_book:
            print(num[:len(prefix)])
            if len(num) >= len(prefix) and prefix == num[:len(prefix)]:
                return False
    return True


# 문자열 정렬
def solution2(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True


# 해쉬 (dictionary)
def solution3(phone_book):
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    for number in phone_book:
        temp = ""
        for n in number:
            temp += n
            if temp in hash_map and number != temp:
                return False
    return True


print(solution3(["119", "97674223", "1195524421"]))
print(solution3(["123", "456", "789"]))
print(solution3(["12", "123", "1235", "567", "88"]))
