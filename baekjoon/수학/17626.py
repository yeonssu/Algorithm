import sys, math

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().strip())
    sq = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
    numbers = [n]
    count = 0
    while numbers:
        count += 1
        temp = set()
        for num in numbers:
            for s in sq:
                if num - s >= 0:
                    temp.add(num - s)
        if 0 in temp:
            break
        numbers = list(temp)
    print(count)
