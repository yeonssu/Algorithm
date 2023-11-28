import sys
input = sys.stdin.readline


if __name__ == "__main__":
    m, d = map(int, input().strip().split())
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d += sum(month[:m])
    answer = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(answer[d % 7])
