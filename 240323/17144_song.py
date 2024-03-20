# 17144_bj(미세먼지 안녕)
'''
https://www.acmicpc.net/problem/17144
'''
def spread():
    dust2 = [[0]*c for _ in range(r)]

    for y in range(r):
        for x in range(c):
            if dust[y][x] not in [0,-1]:
                cnt = 0
                quantity = dust[y][x] // 5
                for d in [0,1], [0,-1], [1,0], [-1,0]: # 네 방향으로 확산
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0 <= dx < c and 0 <= dy < r and dust[dy][dx] != -1: # 범위 안에 있고, 공기청정기가 없을 때
                        dust2[dy][dx] += quantity
                        cnt += 1
                dust[y][x] -= quantity * cnt

    for i in range(r):
        for j in range(c):
            dust[i][j] += dust2[i][j]

def purifying_up(y, x = 1):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    up = y
    d = 0
    value = 0

    while d < 4:
        mx = x + dx[d]
        my = y + dy[d]

        if y == up and x == 0:
            break

        if mx < 0 or mx == c or my < 0 or my == r:
            d += 1
            continue

        dust[y][x], value = value, dust[y][x]
        x = mx
        y = my
#
def purifying_down(y, x = 1):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    down = y
    d = 0
    value = 0

    while d < 4:
        mx = x + dx[d]
        my = y + dy[d]

        if y == down and x == 0:
            break

        if mx < 0 or mx == c or my < 0 or my == r:
            d += 1
            continue

        dust[y][x], value = value, dust[y][x]
        x = mx
        y = my

r, c, t = map(int, input().split())
dust = []
purifier = []
result = 0

for y in range(r):
    dust.append(list(map(int, input().split())))
    for x in range(c):
        if dust[y][x] == -1:
            purifier.append(y)

for i in range(t):
    spread()
    purifying_up(purifier[0])
    purifying_down(purifier[1])


for i in dust:
    result += sum(i)

print(result + 2)