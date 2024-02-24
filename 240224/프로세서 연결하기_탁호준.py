di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def dfs(idx, line_cnt, connecting_cnt): #idx: core의 index(단, 가장자리 제외), line_cnt는 현재까지 연결된 라인 수
    if line_counts[connecting_cnt] > line_cnt:
        line_counts[connecting_cnt] = line_cnt
    if idx == core_cnt: #돌아가
        return
    else:
        i, j = core_pos_list[idx]
        for d in range(4):
            ni, nj = i, j
            cnt_move = 0 #전선 깐 수
            while 0<=ni+di[d]<N and 0<=nj+dj[d]<N:
                ni += di[d] #위치 이동해~
                nj += dj[d]
                if data[ni][nj] != 0: #무언가가 가로막으면 while문 나가!
                    break
                else:               #가로막히지 않으면 전선 깔아
                    data[ni][nj] = 1
                    cnt_move += 1
            else: #안막혔다면 연결된 라인수를 cnt_move만큼 증가시키고, 커넥팅된 수 1개 추가해서 함수 다시 돌려
                dfs(idx+1, line_cnt+cnt_move, connecting_cnt+1)


            #이제 내가 깔았던 전선 다시 치워
            for k in range(1, cnt_move+1):
                data[i+k*di[d]][j+k*dj[d]] = 0
        # 4방향 다 확인후 다른 코어에 대해서 확인
        for x in range(1,N-1):
            if idx + x > core_cnt:
                break
            else:
                dfs(idx + x, line_cnt, connecting_cnt)
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    core_pos_list = [] #core 위치 리스트
    # 가장자리를 제외하고 core 위치들을 찾아서 리스트에 넣기
    for row in range(1,N):
        for col in range(1,N-1):
            if data[row][col] == 1:
                core_pos_list.append([row, col])
    core_cnt = len(core_pos_list)   #전선 연결해 줘야하는 코어 개수
    NN = N*N
    line_counts = [NN]*(core_cnt+1) #연결된 코어 개수가 인덱스로 사용되고 이중 최소 연결된 전선 수들이 들어갈 예정
    dfs(0, 0, 0)
    print(line_counts)
    while line_counts:
        num = line_counts.pop()
        if num != NN:
            print(f'#{tc} {num}')
            break
