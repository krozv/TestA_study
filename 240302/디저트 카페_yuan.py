
##cnt로 함수 호출횟수 카운트 해도 중간에 답이 다르게 나옴 이유는?
##어펜드하면 왜 안되는지?


# 넣었다뻈다 하면 언제 뺼지 조정이 어렵기떄문에 항상 넣기만하기
# 항상 넣기만하려면 dfs에 각자 자기리스트 들고다녀야함
# 자기 리스트 각자 들고다니려면 딱 현재위치에서 어펜드하기


dir = [(1,1),(1,-1),(-1,-1),(-1,1)]
def dfs(i,j,k,lst): # 시작좌표/ 방향/ 카운트
    global maxcnt
    global fst_i,fst_j

    # 종료조건: 현재위치 넣을거라서 위치 + 개수 조건까지 추가하기
    if i == fst_i and j == fst_j and len(lst)> 2 and k ==3 :
        maxcnt = max(maxcnt, len(lst))
        return

    # 현재위치 넣어주기
    if 0<= i < N and 0<= j <N and arr[i][j] not in lst:
        new_lst = lst+[arr[i][j]]
        ####lst.append 해서lst 로 넣으면 답이 틀리게 나옴
        ####lst가 덮어씌워지면 문제가 생기나?

        ni, nj = i+dir[k][0], j+dir[k][1]
        # 그냥가는거 한개, 방향전환 한개
        dfs(ni,nj,k,new_lst)

        if k<3: # k인덱스 안벗어나도록 처리
            #일직선방향가면서 i,j가 바뀌기 때문에 바뀐 방향으로 시작위치 넣어줌
            ni, nj = i + dir[k+1][0], j + dir[k+1][1]
            dfs(ni,nj,k+1,new_lst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = -1
    for x in range(N):
        for y in range(N):
            fst_i, fst_j = x,y
            dfs(x,y,0,[]) # k=0 부터 시작

    print(f'#{tc} {maxcnt}')

