

def inclination(n):
    x1, y1 = atom[n][0]
    inc = []
    for i in range(n+1, N+1):
        x2, y2 = atom[i][0]
        # 기울기가 8인 경우
        if x2 == x1:
            d = abs(y2 - y1) / 2
            if y1 < y2 and [atom[n][1], atom[i][1]] == [0, 1]:
                inc.append([i, 'inf', d])
            elif y2 > y1 and [atom[n][1], atom[i][1]] == [1, 0]:
                inc.append([i, 'inf', d])
        # 그 외
        else:
            a = (y2-y1)/(x2-x1)
            if a in [0, -1, 1]:
                # x, y의 크기 고려해서 델타 계산해야함,,, 제발
                if a == 0:
                    d = abs(x2 - x1) / 2
                    if x1 < x2 and [atom[n][1], atom[i][1]] == [3, 2]:
                        inc.append([i, a, d])
                    elif x1 > x2 and [atom[n][1], atom[i][1]] == [2, 3]:
                        inc.append([i, a, d])
                elif a == -1:
                    d = abs(y2 - y1)
                    if y1 > y2 and [atom[n][1], atom[i][1]] in [[3, 0], [1, 2]]:
                        inc.append([i, a, d])
                    elif y1 < y2 and [atom[n][1], atom[i][1]] in [[0, 3], [2, 1]]:
                        inc.append([i, a, d])
                elif a == 1:
                    d = abs(y2 - y1)
                    if y1 > y2 and [atom[n][1], atom[i][1]] in [[2, 0], [1, 3]]:
                        inc.append([i, a, d])
                    elif y1 < y2 and [atom[n][1], atom[i][1]] in [[0, 2], [3, 1]]:
                        inc.append([i, a, d])
    inf_dict.setdefault(n, inc)     # {원자번호: [다른 원자번호, 원자 간 기울기, 원자 간 거리]}

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    atom = {}
    for i in range(N):
        x, y, d, K = map(int, input().split())
        atom[i+1] = [[x, y], d, K]  # 원자번호를 key로 하여 delta와 K 보유에너지 저장

    energy = 0
    inf_dict = {}
    for i in range(1, N):
        inclination(i)
    # print(inf_dict)
    while True:
        distance = []
        for lst in inf_dict.items():
            for test in lst[1]:
                distance.append(test[-1])
        break

    collide = [0] * (N+1)
    distance = list(set(distance))
    distance.sort()
    # print(distance)
    for dis in distance:
        # print(dis, collide)
        for lst in inf_dict.items():
            if collide[lst[0]] == 0:
                for test in lst[1]:
                    # 충돌이 있는 경우
                    if dis == test[-1] and collide[test[0]] == 0:
                        if collide[lst[0]] == 0:
                            energy += (atom[lst[0]][2])
                            collide[lst[0]] = 1
                        energy += (atom[test[0]][2])
                        collide[test[0]] = 1

    print(f'#{t} {energy}')