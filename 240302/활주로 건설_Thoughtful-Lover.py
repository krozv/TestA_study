'''
활주로를 건설해보자

N*N 크기의 절벽지대에 활주로를 건설하려고 한다.
각 셀의 숫자는 지형의 높이
가로 또는 세로 방향으로 활주로를 건설할 수 있는 가능성

높이가 동등한 구간에서 가능
높이가 다른 구간에서는 높이가 1이고 길이가 x인 경사로를 설치하면 활주로로 사용할 수 있다.
활주로를 건설할 수 있는 경우의 수를 찾아보자

1. 6 ≤ N ≤ 20, N은 정수
2. 경사로의 높이는 항상 1, 길이 X는 정수, 2 <= X <= 4
3. 지형의 높이는 1 이상 6 이하의 정수
4. 동일한 셀에 두 개 이상의 경사로를 겹쳐서 사용할 수는 없다.
'''


# 가로 인덱스를 고정 시켜주고 세로 인덱스를 조사
def checkline_c(x):
    global cnt

    # 조사의 시작점의 초기값은 제일 처음
    sp = cliff[0][x]
    # 같은 고도가 몇 개 있는지 조사
    ground = 1
    # 기본적으로 고도가 차이 나는 곳은 무조건 현재보다 높다고 가정
    reverse = 0
    for j in range(1, N):
        # 시작점과의 고도 차이를 조사
        gap = cliff[j][x] - sp
        # 같은 고도라면 개수를 계속 세어준다.
        if gap == 0:
            ground += 1

        # 만약 현재 고도보다 높다면
        elif gap > 0:
            if reverse == 1 and X <= ground:
                reverse = 0
                # 2차 수정
                ground -= X
            elif reverse == 1:
                return

            # 차이가 1만 날 때는, 지금까지 낮았던 지대가 경사로를 설치할만큼 길이가 되면, 초기화하고 다음으로 넘어감
            if gap == 1 and X <= ground:
                sp = cliff[j][x]
                ground = 1
                continue
            # 만약 경사로를 건설할 수 없다면 return
            return

        # 하지만 현재보다 낮은 지대가 나온다면 일단 reverse 를 1로 해주고 다음 순회로 넘어감 왜냐하면 경사로는 낮은 지대에 지을 수밖에 없기 때문에
        elif gap < 0:
            # 그리고 지대가 바뀌었을 경우에 reverse 가 1이라면 이전에 건설하지 못했던 경사로의 건설 조건을 확인해주어야 함
            if reverse == 1 and X <= ground:
                reverse = 0
                ground -= X
            elif reverse == 1:
                return

            if gap == -1:
                reverse = 1
                sp = cliff[j][x]
                ground = 1
                continue
            return
    # 1차 수정
    if reverse == 1 and X > ground:
        return
    cnt += 1


# 세로 인덱스를 고정 시켜주고 가로 인덱스를 조사
def checkline_r(y):
    global cnt

    sp = cliff[y][0]
    ground = 1
    reverse = 0
    for j in range(1, N):
        gap = cliff[y][j] - sp
        if gap == 0:
            ground += 1
        elif gap > 0:
            if reverse == 1 and X <= ground:
                reverse = 0
                ground -= X
            elif reverse == 1:
                return

            if gap == 1 and X <= ground:
                sp = cliff[y][j]
                ground = 1
                continue
            return
        elif gap < 0:
            if reverse == 1 and X <= ground:
                reverse = 0
                ground -= X
            elif reverse == 1:
                return

            if gap == -1:
                reverse = 1
                sp = cliff[y][j]
                ground = 1
                continue
            return
    # 1차 수정
    if reverse == 1 and X > ground:
        return
    cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    cliff = [list(map(int, input().split())) for _ in range(N)]
    # 활주로 건설 가능 개수를 조사
    cnt = 0

    for i in range(N):
        '''하나는 세로방향을 고정하고 가로방향을 탐색
        하나는 가로방향을 고정하고 세로방향을 탐색'''
        checkline_c(i)
        checkline_r(i)

    print(f'#{tc} {cnt}')