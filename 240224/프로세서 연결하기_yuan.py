

import copy

di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]

#상하좌우 체크해서 i또는 j가 0일때까지의 최소 경로 찾는 함수
def find_bfs(i,j,N,arr):
    f_cnt = 0
    q = []
    q.append((i, j))
    while q:
        i,j = q.pop()
        if i==0 or j ==0:
            return f_cnt,i,j # 최소 횟수랑 그떄의 좌표값 리턴

        else:
            for k in range(4):
                ni, nj = i+di[k], j + dj[k]
                if 0<= ni< N and 0< nj< N and not arr[ni][nj]:
                    q.append((ni,nj))
                    arr[ni][nj] = 1
                    f_cnt +=1
    
    return False 
    
# 방문 현황, 확인개수, 전석연결코어개수, 전선개수, core 인덱스->c_lst[a]로 표현
def dfs(arr, chk_core, on_core, cnt, a):
    global mincnt
    global maxcore
    
    if chk_core == cn:
        if on_core>= maxcore and cnt < mincnt:
            maxcore, mincnt = on_core, cnt
        return maxcore, mincnt

    else:
        x, y = c_lst[a]  # 현재 코어위치 인덱스로 표시

        if c_lst[a] != '*': # 방문한적 없음 
            a = find_bfs(x,y,N,arr)
            if a:
                f_cnt, i, j = a
                arr_v = copy.deepcopy(arr) # 중간 저장

                # 현위치x,y / 0되는 좌표 i,j/ 이동만큼 arr_v 행렬을 1로 바꿔주기
                if i<x: # 상
                    for k in range(i-1,-1,2):
                        arr_v[k][j] = 1
                elif i>x: # 하
                    for k in range(i+1,-1,2):
                        arr_v[k][j] = 1
                elif j<y: # 좌
                    for k in range(j-1,-1,2):
                        arr_v[i][j] = 1
                elif j<y: # 우
                    for k in range(j+1,-1,2):
                        arr_v[i][j] = 1
    
                c_lst[a] = '*'  # 방문표시
                for x in range(-1,2,2):
                    if 0<= a+x <N:
                        dfs(arr_v, chk_core+1, on_core+1, cnt+f_cnt, a+x)
                # if 0<= a-1 < N:
                #     dfs(arr_v, chk_core+1, on_core+1, cnt+f_cnt, a-1)
                # 
                # if 0<= a+1 < N:
                #     dfs(arr_v, chk_core+1, on_core+1, cnt+f_cnt, a+1)

            # 가능한 좌표값 없을때 
            else:
                c_lst[a] = '*'  # 방문표시
                for x in range(-1,2,2):
                    if 0<= a+x <N:
                        dfs(arr, chk_core+1, on_core, cnt, a+x)
                
        #방문한 적 있을떄
        else:
            for b in range(-1, 2, 2):
                if 0 <= a + b < N:
                    dfs(arr, chk_core, on_core, a + b)

import sys
sys.stdin = open('sample_input.txt', 'r')
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    maxcore = 0
    mincnt = N*N # 최대 cnt
    arr = [list(map(int,input().split())) for _ in range(N)]

    c_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and i != 0 and j!=0 :
                c_lst.append((i,j))

    cn = len(c_lst) #0아닌 코어개수

    fin_max_score = 0
    fin_min_cnt = N*N
    for aa in range(cn):
        max, min = dfs(arr, 0, 0, 0, aa) # 인덱스 0~12부터 시작점 정하rl
        if max >= fin_max_score and min < fin_min_cnt:
            fin_min_cnt = min
    print(f'#{tc} {min}')