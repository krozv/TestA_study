# 무선 충전 SWEA 5644
T = int(input())
for case in range(1, T+1):
    # 총 이동시간 m, BC의 개수 n
    m, n = map(int, input().split())
    # a(1,1)와 b(10,10)의 이동 정보 (m 개)
    # 0 1 2 3 4 -> 정지 상 우 하 좌
    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]
    # 충전기(BC) 정보 (n 줄)
    bc_info = [list(map(int, input().split())) for _ in range(n)]

    a = [1, 1]
    ss_a = 0
    b = [10, 10]
    ss_b = 0
    for i in range(m+1):      # m 시간만큼 반복
        a_bc = [0] * n
        b_bc = [0] * n
        for j in range(n):  # n 개의 bc 반복
            # 좌표 x, y, 충전 범위 c, 처리량 p
            y, x, c, p = bc_info[j][0], bc_info[j][1], bc_info[j][2], bc_info[j][3]
            # 거리 측정 및 닿는 bc 목록 생성
            da = abs(a[0] - x) + abs(a[1] - y)
            db = abs(b[0] - x) + abs(b[1] - y)
            if da <= c and db <= c:
                a_bc[j] += p
                b_bc[j] += p
            elif da <= c:
                a_bc[j] += p
            elif db <= c:
                b_bc[j] += p
        # 최대로 충전하는 경우 선택
        max_distribution = 0
        max_a = 0
        max_b = 0
        for x in range(n):
            for y in range(n):
                a_now = a_bc[x]
                b_now = b_bc[y]
                if x == y and a_now == b_now:
                    a_now //= 2
                    b_now //= 2
                if max_distribution < a_now + b_now:
                    max_distribution = a_now + b_now
                    max_a = a_now
                    max_b = b_now
        ss_a += max_a
        ss_b += max_b
        # 좌표 이동 (다음 시간대)
        if i < m:
            a[0] += dx[a_move[i]]
            a[1] += dy[a_move[i]]
            b[0] += dx[b_move[i]]
            b[1] += dy[b_move[i]]

    print(f'#{case}', ss_a + ss_b)
