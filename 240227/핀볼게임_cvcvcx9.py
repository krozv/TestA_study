T = int(input())
'''
호준, 호진코드 보고 다시품
'''
# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
direction = [
    # 1을 만났을 때
    {0: 2, 1: 0, 2: 3, 3: 1},
    # 2를 만났을 때
    {0: 2, 1: 3, 2: 1, 3: 0},
    # 3을 만났을 때
    {0: 1, 1: 3, 2: 0, 3: 2},
    # 4를 만났을 때
    {0: 3, 1: 2, 2: 0, 3: 1},
    # 5를 만났을 때
    {0: 2, 1: 3, 2: 0, 3: 1},
]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    worm_hole_li = [[] for _ in range(5)]
    worm_hole_dict = {}
    cnt = 0
    # 웜홀들의 위치를 찾아서, list에 저장
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 5:
                worm_hole_li[matrix[i][j] - 6].append((i, j))
    # list에 저장했던 웜홀을 꺼내, 서로 연결시킴
    for worm_hole in worm_hole_li:
        if worm_hole:
            worm_hole_dict[worm_hole[0]] = worm_hole[1]
            worm_hole_dict[worm_hole[1]] = worm_hole[0]
    # 가장 높은 점수를 저장할 변수
    max_cnt = 0
    # 좌표에 값이 0인경우에만 시작점으로 사용 가능하다.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                # 시작하는 방향은 네개 모두 가능하다
                for d in range(4):
                    cnt = 0
                    ni = i + di[d]
                    nj = j + dj[d]
                    # ni가 i가 아니고, nj가 j가 아닌경우에
                    while i != ni or j != nj:
                        # 벽이라면 방향을 반대로 돌리고, 카운트 +1
                        if ni < 0 or ni >= N or nj < 0 or nj >= N:
                            d = (d + 2) % 4
                            cnt += 1
                        # 만약 블록이라면, 블록에 해당하는 방향으로 방향을 변경
                        elif matrix[ni][nj] in [1, 2, 3, 4, 5]:
                            # 해당 블록에 해당하는 방향으로 전환
                            d = direction[matrix[ni][nj]-1][d]
                            cnt += 1
                        # 웜홀인 경우에는, 연결된 웜홀로 텔레포트시킴
                        elif matrix[ni][nj] > 5:
                            ni, nj = worm_hole_dict[(ni, nj)]
                        # 만약 블랙홀이면
                        elif matrix[ni][nj] == -1:
                            # 점수세기 끝
                            break
                        # 방향만큼 이동시킴
                        ni += di[d]
                        nj += dj[d]
                    if max_cnt < cnt:
                        max_cnt = cnt
    print(max_cnt)