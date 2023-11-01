import sys, re
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        word = input().strip()
        pattern = r"^[A-F]?A+F+C+[A-F]?$"
        if re.match(pattern, word):
            print("Infected!")
        else:
            print("Good")
