# 원자 소멸 시뮬레이션 SWEA 5648
T = int(input())
for case in range(1, T+1):
    # 원자의 개수
    n = int(input())
    # 원자의 위치 x, y / 이동 방향 d / 보유 에너지 k
    x = [0] * n
    y = [0] * n
    d = [0] * n
    k = [0] * n
    for i in range(n):
        x[i], y[i], d[i], k[i] = map(int, input().split())

    # 0 1 2 3 -> 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    min_pos = [[[], 5000] for _ in range(n)]
    for i in range(n):
        min_distance = 5000
        for j in range(n):
            if i == j:
                continue
            if d[i] == 0:
                if y[i] < y[j]:
                    if (
                        (2 <= d[j] <= 3 and abs(x[i] - x[j]) == abs(y[i] - y[j])) or
                        (d[j] == 1 and x[i] == x[j])
                    ):
                        if min_distance > abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_distance = abs(x[i] - x[j]) + abs(y[i] - y[j])
                            min_pos[i] = [[j], min_distance, k[i], i]
                        elif min_distance == abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_pos[i][0].append(j)
            elif d[i] == 1:
                if y[i] > y[j]:
                    if (
                        (2 <= d[j] <= 3 and abs(x[i] - x[j]) == abs(y[i] - y[j])) or
                        (d[j] == 0 and x[i] == x[j])
                    ):
                        if min_distance > abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_distance = abs(x[i] - x[j]) + abs(y[i] - y[j])
                            min_pos[i] = [[j], min_distance, k[i], i]
                        elif min_distance == abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_pos[i][0].append(j)
            elif d[i] == 2:
                if x[i] > x[j]:
                    if (
                        (0 <= d[j] <= 1 and abs(x[i] - x[j]) == abs(y[i] - y[j])) or
                        (d[j] == 3 and y[i] == y[j])
                    ):
                        if min_distance > abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_distance = abs(x[i] - x[j]) + abs(y[i] - y[j])
                            min_pos[i] = [[j], min_distance, k[i], i]
                        elif min_distance == abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_pos[i][0].append(j)
            elif d[i] == 3:
                if x[i] < x[j]:
                    if (
                        (0 <= d[j] <= 1 and abs(x[i]-x[j]) == abs(y[i]-y[j])) or
                        (d[j] == 2 and y[i] == y[j])
                    ):
                        if min_distance > abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_distance = abs(x[i] - x[j]) + abs(y[i] - y[j])
                            min_pos[i] = [[j], min_distance, k[i], i]
                        elif min_distance == abs(x[i] - x[j]) + abs(y[i] - y[j]):
                            min_pos[i][0].append(j)
    print(min_pos)
    min_pos.sort(key=lambda f: f[1])
    emitted = 0
    print(min_pos)
    for pos in min_pos:
        if pos and pos[0]:
            emitted += pos[2]
            for j in pos[0]:
                if pos and pos[0]:
                    emitted += pos[2]
                    pos = 0
            pos = 0
        print(min_pos, emitted)

    print(f'#{case}', emitted)
