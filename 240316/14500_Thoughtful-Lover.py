'''
14500. 테트로미노

정사각형 4개를 이어붙인 테트로미노
N, M 칸 위에 테트로미노 하나를 놓을 때
놓인 칸에 쓰인 수들의 합 중 최대는
단 회전이나 대칭 이동은 가능
'''


# 4칸짜리 도형을 이리저리 놓아보는 함수 tetromino
def tetromino(y, x, sub_sum, cnt):
    global max_sum

    # 먼저 현재 위치를 체크하고 구간합에 적힌 수를 더함
    sub_sum += paper[y][x]
    checked[y][x] = 1

    # 4칸을 모두 채웠을 때 구간합이 최대합보다 크면 최대합 값을 갱신
    if cnt == 4:
        if max_sum < sub_sum:
            max_sum = sub_sum
        checked[y][x] = 0
        return

    # 현재 칸에서 상하좌우로 움직임
    for di, dj in [1, 0], [0, 1], [-1, 0], [0, -1]:
        ni = y+di
        nj = x+dj

        # 샹햐좌우가 범위를 벗어나지 않고 아직 방문하지 않았으면, 다음 위치로 방문
        if 0<=ni<N and 0<=nj<M and checked[ni][nj] == 0:
            tetromino(ni, nj, sub_sum, cnt+1)
    # 탐색을 모두 마쳤다면 방문 초기화
    checked[y][x] = 0


# 볼록할 철 모양 테트로미노를 확인하기 위한 함수 mountain
def mountain():
    global max_sum

    # 위에 것은 새로로 서 있는 볼록할 철 모양 테트로미노를 잡아냄
    for k in range(2, N):
        for l in range(M):
            sub_sum = 0
            # 배열 위를 순회하며 세로 3개를 더해주고
            for m in range(3):
                sub_sum += paper[k-m][l]
            # 조건이 맞으면 가운데 뾰족한 부분을 더해주고 최대합 값과 비교해서 갱신
            if l-1 > -1:
                sub_sum += paper[k-1][l-1]
                if max_sum < sub_sum:
                    max_sum = sub_sum
                sub_sum -= paper[k-1][l-1]
            if l+1 < M:
                sub_sum += paper[k-1][l+1]
                if max_sum < sub_sum:
                    max_sum = sub_sum
                sub_sum -= paper[k-1][l+1]

    # 아래 것은 가로로 누워 있는 볼록할 철 모양 테트로미노를 잡아냄
    for n in range(2, M):
        for o in range(N):
            sub_sum = 0
            for p in range(3):
                sub_sum += paper[o][n-p]
            if o-1 > -1:
                sub_sum += paper[o-1][n-1]
                if max_sum < sub_sum:
                    max_sum = sub_sum
                sub_sum -= paper[o-1][n-1]
            if o+1 < N:
                sub_sum += paper[o+1][n-1]
                if max_sum < sub_sum:
                    max_sum = sub_sum
                sub_sum -= paper[o+1][n-1]


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
checked = [[0]*M for _ in range(N)]
# 테트로미노를 놓을 때 얻을 수 있는 최대값을 저장할 변수 max_sum, 초기값은 네 개짜리 테트로미노를 놓을 때 최소값 4
max_sum = 4

for i in range(N):
    for j in range(M):
        tetromino(i, j, 0,1)

mountain()

print(max_sum)

'''
처음에는 기준점을 하나 잡고 연달아 4칸을 이동해서 하는 방식을 생각했는데, 그렇게 하니까 저 볼록할 철 모양이 최대인 값을 잡아내지 못했다.
그래서 mountain에서 완탐해서 볼록할 철 모양 테트로미노를 잡았다 휴
'''