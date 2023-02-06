import sys
input = sys.stdin.readline
T = int(input().strip())

for t in range(T):
    number_book = []
    N = int(input().strip())
    for n in range(N):
        number_book.append(input().strip())

    answer = "YES"
    number_book.sort()
    for n in range(N):
        if n+1 < len(number_book):
            if number_book[n+1][:len(number_book[n])] == number_book[n]:
                answer = "NO"

    print(answer)
