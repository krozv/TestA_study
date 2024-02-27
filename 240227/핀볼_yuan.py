
# 상 하 좌 우
d = (
    (0, 1),  # 0 동
    (1, 0),  # 1 남
    (0, -1),  # 2 서
    (-1, 0)  # 3 북
)
def f(x,y,k):
    cnt = 0
    while True:
        ni = x+ d[k][0]
        nj = y+ d[k][1]
        if 0<= ni < N and 0<= nj <N:

            # 끝내는 조건
            if (ni, nj) == (first_i, first_j):
                return cnt

            # 블랙홀
            elif arr[ni][nj] == -1:
                return cnt

            # 빈공간
            elif arr[ni][nj] == 0:
                continue
            # 블록
            elif arr[ni][nj] in range(1,6):
                cnt +=1
                k = dicblock[arr[ni][nj]-1][k]

            # 웜홀
            elif arr[ni][nj] in range(6,11):
                idx = arr[ni][nj]
                if (ni, nj) == dicworm[idx][0]:
                    ni, nj = dicworm[idx][1]
                else:
                    ni, nj = dicworm[idx][0]

        # 레인지 밖으로 나갈때, 즉 벽에 부딫힐때
        else:# 상,하,좌,우  -> 반대로 방향 하, 상, 좌, 우가기
            k = (k+2) % 4
            cnt +=1



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = 0

    # 블록 만날때 #k= 1,2,3,4, / 블록이 1,2,3,4,5 -> 5개씩
    dicblock = (
        (2, 0, 3, 1),
        (2, 3, 1, 0),
        (1, 3, 0, 2),
        (3, 2, 0, 1),
        (2, 3, 0, 1)
    )
    # 웜홀 #k= 1,2,3,4, / 블록이 6,7,8,9,10 -> 5개씩
    key = [i for i in range(6, 11)]
    value = [[] for _ in range(5)]
    dicworm = dict(zip(key, value))

    # 웜홀 넣기
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] <= 10:
                dicworm[arr[i][j]].append((i, j))

    for i in range(N):
        for j in range(N):
            if arr[i][j] ==0:
                for k in range(4):
                    first_i, first_j = i, j
                    cnt = f(i,j,k)
                    maxcnt = max(cnt,maxcnt)

    print(f'{tc} {maxcnt}')

