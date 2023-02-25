import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().strip().split())

city = []
for n in range(N):
    city.append(list(map(int, input().strip().split())))

location_chicken = []
location_house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            location_chicken.append((i, j))
        if city[i][j] == 1:
            location_house.append((i, j))

answer = 999999999
for chosen_chicken in combinations(location_chicken, M):
    city_chicken_street = 0
    for house_x, house_y in location_house:
        chicken_street = 999999999
        for chicken_x, chicken_y in chosen_chicken:
            distance = abs(chicken_x - house_x) + abs(chicken_y - house_y)
            chicken_street = min(chicken_street, distance)
        city_chicken_street += chicken_street
    answer = min(answer, city_chicken_street)

print(answer)
