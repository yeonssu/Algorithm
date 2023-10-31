import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    country = []
    people = 0
    for _ in range(n):
        x, a = map(int, input().strip().split())
        country.append((x, a))
        people += a

    country.sort(key=lambda x: x[0])
    count = 0
    for x, a in country:
        count += a
        if count >= people / 2:
            print(x)
            break
