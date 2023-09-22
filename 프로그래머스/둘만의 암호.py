from string import ascii_lowercase


def solution(s, skip, index):
    answer = ''
    hash_map = {}
    for sk in skip:
        hash_map[sk] = 1
    for alphabet in s:
        alphabet_ascii = ord(alphabet)
        i = index
        while i != 0:
            alphabet_ascii += 1
            if alphabet_ascii > 122:
                alphabet_ascii -= 26
            if chr(alphabet_ascii) in hash_map:
                continue
            else:
                i -= 1
        answer += chr(alphabet_ascii)
    return answer


def solution2(s, skip, index):
    answer = ''
    alphabet = set(ascii_lowercase)
    alphabet = alphabet - set(skip)
    alphabet = sorted(alphabet)

    hash_map = {}
    for idx, alpha in enumerate(alphabet):
        hash_map[alpha] = idx

    for i in s:
        answer += alphabet[(hash_map.get(i) + index) % len(alphabet)]

    return answer


print(solution2("aukks", "wbqd", 5))
