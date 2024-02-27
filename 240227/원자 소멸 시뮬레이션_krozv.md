# 원자 소멸 시뮬레이션

## 완전탐색

while문 사용 -> 원자가 1개도 남지 않을 때까지 반복 -> 시간초과 뜰 것 같은데
1초에 한번씩 전체 이동 확인
위치하려는 자리에 원자가 있을 경우 +1
1 이상인 원자 전부 삭제
원자가 한 개도 없을때까지 반복

```python
def collide():
    pass
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0] * 2001 for _ in range(2001)]
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    atom = {}
    for i in range(N):
        x, y, d, K = map(int, input().split())
        atom[i+1] = [d, K]  # 원자번호를 key로 하여 delta와 K 보유에너지 저장
        arr[x+1000][y+1000] = -(i+1)    # -key를 저장
    print(atom)
    print(arr)
    energy = 0
    while sum(arr) != 0:
        collide()
    print(energy)
```
## greedy

원자 간의 거리가 제일 짧은 것부터 찾아서 충돌시키고 없앰
계속 돌려
또 짧은 거 찾아서 충돌시키고 없앰
양방향을 굳이 봐야하나?
row:
    원자가 존재하고 and delta의 순서가 2, 3일 경우 충돌
col:
    원자가 존재하고 and delta의 순서가 0, 1일 경우 충돌
그냥 기울기 계산해서 빼버리면?

```python


def inclination(n):
    x1, y1 = atom[n][0]
    inc = []
    for i in range(n+1, N+1):
        x2, y2 = atom[i][0]
        # 기울기가 8인 경우
        if x2 == x1:
            d = abs(y2 - y1) / 2
            if y1 < y2 and [atom[n][1], atom[i][1]] == [0, 1]:
                inc.append([i, d])
            elif y1 > y2 and [atom[n][1], atom[i][1]] == [1, 0]:
                inc.append([i, d])
        # 그 외
        else:
            a = (y2-y1)/(x2-x1)
            # 기울기가 0인 경우
            if a == 0:
                d = abs(x2 - x1) / 2
                if x1 < x2 and [atom[n][1], atom[i][1]] == [3, 2]:
                    inc.append([i, d])
                elif x1 > x2 and [atom[n][1], atom[i][1]] == [2, 3]:
                    inc.append([i, d])
            # 기울기가 -1인 경우
            elif a == -1:
                d = abs(y2 - y1)
                if y1 > y2 and [atom[n][1], atom[i][1]] in [[3, 0], [1, 2]]:
                    inc.append([i, d])
                elif y1 < y2 and [atom[n][1], atom[i][1]] in [[0, 3], [2, 1]]:
                    inc.append([i, d])
            # 기울기가 1인 경우
            elif a == 1:
                d = abs(y2 - y1)
                if y1 > y2 and [atom[n][1], atom[i][1]] in [[2, 0], [1, 3]]:
                    inc.append([i, d])
                elif y1 < y2 and [atom[n][1], atom[i][1]] in [[0, 2], [3, 1]]:
                    inc.append([i, d])
    inc_dict.setdefault(n, inc)     # {원자번호: [부딪힌 원자번호, 원자 간 거리]}

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())

    atom = {}
    for i in range(N):
        x, y, D, K = map(int, input().split())
        atom[i+1] = [[x, y], D, K]  # 원자번호를 key로 하여 delta와 K 보유에너지 저장

    energy = 0
    inc_dict = {}
    # 원자 간 기울기를 계산
    for i in range(1, N):
        inclination(i)

    #
    while True:
        distance = []
        for inc in inc_dict.values():
            # inc : [i번 원자와 충돌한 원자 번호, 원자 거리]
            # 예) inc = [[2, 1000.0], [3, 1000], [4, 1000]]
            for dis in inc:
                # dis : 충돌한 원자 거리
                distance.append(dis[-1])
        break

    # 충돌 거리가 짧은 순서로 정렬
    distance = list(set(distance))
    distance.sort()

    # 충돌한 원자들 구분하는 배열 (=visited)
    collide = [0] * (N + 1)

    for dis in distance:
        # dis : 충돌한 원자 거리
        for inc in inc_dict.items():
            # inc : (i번 원자, [i번 원자와 충돌한 원자 번호, 원자 거리])
            if not collide[inc[0]]:    # i번 원자가 충돌하지 않았다면
                for other in inc[1]:    # 다른 원자를 하나씩 꺼내서 계산
                    # 충돌이 있는 경우: 충돌한 원자 거리(dis)가 같고, 해당 원자가 충돌하지 않은 원자일 경우
                    if dis == other[-1] and not collide[other[0]]:
                        # i번 원자에 방문표시 해주고, 에너지 추가
                        if collide[inc[0]] == 0:
                            energy += (atom[inc[0]][2])
                            collide[inc[0]] = 1
                        # i번 원자와 충돌한 원자에 방문표시 하고, 에너지 추가
                        collide[other[0]] = 1
                        energy += (atom[other[0]][2])

    print(f'#{t} {energy}')
```