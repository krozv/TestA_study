



def dfs(i,N,sumN): # 넣으려는 사람 인덱스,총 인원수(반복횟수), 현재 합
    global min_heightgap
    if i == N:
        if sumN >= B_height:
            min_heightgap = min(min_heightgap, sumN-B_height)
        return

    else:
        # 현재 사람 키 넣어서 돌리기
        dfs(i+1,N,sumN+N_lst[i])
        # 안넣어서 돌리기
        dfs(i+1,N,sumN)


T = int(input())
for tc in range(1,T+1):

    N, B_height = map(int, input().split()) # 사람수, 선반높이
    N_lst = list(map(int, input().split())) # 사람리스트
    # B_height 의 최대값은 sum(N_lst)
    min_heightgap = 2 * B_height # minheightgap 이 가질수 있는 최대값

    dfs(0,N,0) # 사람수 1명~ N명까지 넣을지 말지 결정하기
    print(f'#{tc} {min_heightgap}')