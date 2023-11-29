import sys
input = sys.stdin.readline


if __name__ == "__main__":
    t = int(input().strip())
    apartment = [[0] * 15 for _ in range(15)]
    apartment[0] = list(range(15))
    for i in range(1, 15):
        for j in range(15):
            apartment[i][j] = sum(apartment[i - 1][:j + 1])

    for _ in range(t):
        k = int(input().strip())
        n = int(input().strip())
        print(apartment[k][n])
