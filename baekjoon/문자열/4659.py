import sys
input = sys.stdin.readline


def isVowel(word):
    if word in ["a", "e", "i", "o", "u"]:
        return True
    return False


def check1():
    for i in range(len(password)):
        if isVowel(password[i]):
            return True
    return False


def check2():
    for i in range(len(password)):
        if i + 2 < len(password) and ((isVowel(password[i]) and isVowel(password[i + 1]) and isVowel(password[i + 2]))
            or (not isVowel(password[i]) and not isVowel(password[i + 1]) and not isVowel(password[i + 2]))):
            return False
    return True


def check3():
    for i in range(len(password)):
        if i + 1 < len(password):
            if password[i] == password[i + 1]:
                if password[i] == "e" or password[i] == "o":
                    return True
                return False
    return True


if __name__ == "__main__":
    while True:
        password = input().strip()
        if password == "end":
            break

        result = "<" + password + "> is "
        if not check1() or not check2() or not check3():
            result += "not "
        result += "acceptable."
        print(result)
