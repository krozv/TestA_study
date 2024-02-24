# 프로세서 연결하기
def f(i, p, l):
    '''
    i: 현재 탐색 중인 프로세서 인덱스
    p: 연결 성공한 프로세서 개수
    l: 연결한 전선 개수
    '''
    # 프로세서 N까지 연결 시도 종료
    # 프로세서 하나씩 연결
    global max_node, min_line
    if len(core)-i < max_node-p:
        return
    if i == len(core):
        if max_node < p:
            max_node = p
            min_line = l
        elif max_node == p:
            if min_line > l:
                min_line = l
        return
    x, y = core[i]
    v[x][y] = 1

    for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        for k in range(1, N+1):
            ni = x + d[0] * k
            nj = y + d[1] * k
            # 세로로 전선 연결 성공
            if ni < 0 or ni == N:
                for n in range(1, k):
                    mi = ni-d[0]*n
                    mj = nj
                    v[mi][mj] = 1
                f(i+1, p+1, l+k-1)
                for n in range(1, k):
                    mi = ni - d[0] * n
                    mj = nj
                    v[mi][mj] = 0
                break
            # 가로로 전선 연결 성공
            if nj < 0 or nj == N:
                for n in range(1, k):
                    mi = ni
                    mj = nj - d[1] * n
                    v[mi][mj] = 1
                f(i+1, p+1, l+k-1)
                for n in range(1, k):
                    mi = ni
                    mj = nj - d[1] * n
                    v[mi][mj] = 0
                break
            # 연결 실패
            if arr[ni][nj] or v[ni][nj]:
                f(i+1, p, l)
                break


import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    core = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                core.append([i, j])
    v = [[0] * N for _ in range(N)]
    max_node = 0
    min_line = N * N
    f(0, 0, 0)
    print(f'#{t} {min_line}')
