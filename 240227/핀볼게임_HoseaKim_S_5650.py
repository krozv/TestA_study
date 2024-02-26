# 핀볼 게임

T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 웜홀 쌍 찾기
    t = [[] for _ in range(5)]
    for i in range(n):
        for j in range(n):
            if 6 <= arr[i][j] <= 10:
                t[arr[i][j]-6].append((i, j))
    hole_pair = {}
    for i in range(5):
        if t[i]:
            hole_pair[t[i][0]] = t[i][1]
            hole_pair[t[i][1]] = t[i][0]

    # <key>
    # 1: ↙, 2: ↖, 3: ↗, 4: ↘, 5: □
    # 6~10 : 웜홀쌍, -1 : 블랙홀 (최대 5개)
    # <index 및 value>
    # 0: →, 1: ↓, 2: ←, 3: ↑
    dir = [{1: 2, 2: 2, 3: 1, 4: 3, 5: 2}, 
           {1: 0, 2: 3, 3: 3, 4: 2, 5: 3}, 
           {1: 3, 2: 1, 3: 0, 4: 0, 5: 0}, 
           {1: 1, 2: 0, 3: 2, 4: 1, 5: 1}]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_score = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
    # i, j = [2, 3]
                for d in range(4):
                    score = 0
                    ni = i + dx[d]
                    nj = j + dy[d]
                    while ni != i or nj != j:
                        if ni < 0 or ni >= n or nj < 0 or nj >= n:
                            d = (d + 2) % 4
                            score += 1
                        elif arr[ni][nj] == -1:
                            break
                        elif 1 <= arr[ni][nj] <= 5:
                            d = dir[d][arr[ni][nj]]
                            score += 1
                        elif 6 <= arr[ni][nj] <= 10:
                            ni, nj = hole_pair[(ni, nj)]
                        ni += dx[d]
                        nj += dy[d]
                    if max_score < score:
                        max_score = score

    print(f'#{case}', max_score)
