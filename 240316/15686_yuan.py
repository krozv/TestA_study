def f(arr):
    global home
    # for i in arr:
    #     print(i)
    # print()

    min_res = 0
    now_chk_lst = [] # 현재 치킨집 리스트
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==2:
                now_chk_lst.append((i,j))

    for h1,h2 in home:#w집좌표
        res=2*N
        for c1,c2 in now_chk_lst:
            d = abs(h1-c1)+abs(h2-c2)
            res = min(res,d)
        min_res+=res # 가장 작은 거리 더하기

    return min_res



def dfs(i,n): # i는 현재 확인중인 인덱스 n 은 선택한(없앨) 개수
    global min_d

    if n == k:
        # for i in arr:
        #     print(i)
        # print()
        min_res = f(arr)
        min_d = min(min_d, min_res)
        return

    if i == chk: # 치킨개수 되면 리턴
        return

    else:
        x,y = chk_lst[i][0], chk_lst[i][1]
        arr[x][y] = 3 # 치킨 폐업
        dfs(i+1,n+1)
        arr[x][y] = 2 # 원상복구
        dfs(i+1,n) # 선택안하고 돌리기


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

home = []
chk_lst = []
chk = 0 # 치킨집 개수
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chk_lst.append((i,j))
            chk+=1
        if arr[i][j] ==1:
            home.append((i,j))

min_d = N*N*N
#M 개만 살리니까 없앨 k = chk-M 선택할것
k = chk-M
dfs(0,0)
print(min_d)