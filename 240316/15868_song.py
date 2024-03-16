# 15868_치킨배달
'''
https://www.acmicpc.net/problem/15686
x, y값 따로 받기
너무 어렵게 생각했던 듯
'''

from itertools import combinations
import copy

# 방법 1 - 시간 오래 걸림
# def measurement(comb):
#     distant = 0
#     least_chicken = [i for i in chicken if i not in comb]
#     for h in house:
#         distant += min([abs(h[0]-x[0]) + abs(h[1]-x[1]) for x in least_chicken])

#     global result
#     if result > distant:
#         result = distant

# n, m = map(int, input().split())

# area = []
# chicken = []
# house = []
# result = 10000000000

# for y in range(n):
#     area.append(list(map(int, input().split())))
#     for x in range(n):
#         if area[y][x] == 1:
#             house.append([x, y])
#         elif area[y][x] == 2:
#             chicken.append([x, y])

# for c in combinations(chicken, len(chicken)-m):
#     area2 = copy.deepcopy(area)
#     for i in c:
#         area2[i[1]][i[0]] = 0
#     measurement(c)

# print(result)

# 방법 2
from itertools import combinations
n, m = map(int, input().split())

area = []
chicken = []
house = []
result = 10000000000

for y in range(n):
    area.append(list(map(int, input().split())))
    for x in range(n):
        if area[y][x] == 1:
            house.append([x, y])
        elif area[y][x] == 2:
            chicken.append([x, y])

for c in combinations(chicken, m):
    distance = 0
    for x1, y1 in house:
        distance += min([abs(x1-x2) + abs(y1-y2) for x2, y2 in c])
    if result > distance:
        result = distance


print(result)