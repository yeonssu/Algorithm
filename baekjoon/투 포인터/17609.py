import sys

input = sys.stdin.readline


def is_palindrome(w, left, right):
    while left < right:
        if w[left] == w[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def is_pseudo_palindrome(word):
    if word[:] == word[::-1]:
        return 0
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            left_check = is_palindrome(word, left + 1, right)
            right_check = is_palindrome(word, left, right - 1)
            if left_check or right_check:
                return 1
            else:
                return 2
    return 1


if __name__ == "__main__":
    for _ in range(int(input())):
        print(is_pseudo_palindrome(input().strip()))
