# 핀볼 게임
### 코드
```python
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
#1~5번의 블록을 부딪혔을때, 움직이고 있던 방향에 따라 변경될 방향을 알려줄 이중 딕셔너리
dir_change = {1:{0:2,1:0,2:3,3:1},
              2:{0:2,1:3,2:1,3:0},
              3:{0:1,1:3,2:0,3:2},
              4:{0:3,1:2,2:0,3:1},
              5:{0:2,1:3,2:0,3:1}}
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #영역 길이
    data = [list(map(int, input().split())) for _ in range(N)]
    possible_pos = [] #출발 가능한 위치 찾기
    worm_hole_list = [[] for _ in range(11)] #제대로 쓸건 6~10번 인덱스긴함
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                possible_pos.append([i,j])
            if data[i][j] > 5: #웜홀 리스트에 추가해주기
                worm_hole_list[data[i][j]].append((i,j))
    worm_hole_dict = {}
    #한쪽 웜홀을 찾을 시 다른 쪽 웜홀로 빠져 나올 수 있게 딕셔너리 생성
    for i, worm_hole in enumerate(worm_hole_list):
        if worm_hole:
            worm_hole_dict[i] = {worm_hole[0] : worm_hole[1], worm_hole[1]:worm_hole[0]}

    max_score = 0
    for i, j in possible_pos: #위치 꺼내오기
        start_i, start_j = i, j #시작 위치
        for d in range(4):  #4방향 모두 가기
            score = 0       #게임 점수
            ni, nj =i, j #현재 위치(이거를 안하고 그냥 i, j를 사용하면 문제가 발생했었음!!!!!)
            while True: #본격적으로 핀볼게임 시작
                ni += di[d] #현재 방향으로 위치 이동
                nj += dj[d]
                if 0<=ni<N and 0<=nj<N: #정상범위에 있는 경우
                    if data[ni][nj] == -1: #블랙홀에 도달한 경우
                        break
                    elif ni == start_i and nj == start_j:
                        break
                    elif data[ni][nj] in [1,2,3,4,5]: #1~5번 블록에 해당하는 경우
                        d = dir_change[data[ni][nj]][d] #방향변경
                        score += 1
                    elif data[ni][nj] in [6,7,8,9,10]: #웜홀을 만나는 경우
                        ni, nj = worm_hole_dict[data[ni][nj]][(ni,nj)] #다른 웜홀 위치로 이동
                else:
                    d = (d+2)%4 #범위를 벗어난 경우(벽에 부딪힌경우) 방향을 180도 변경
                    score += 1
            if max_score < score:
                max_score = score
    print(f'#{tc} {max_score}')
```