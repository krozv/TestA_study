# 2105. 디저트 카페

### 코드
695ms
```python
#0:오른쪽위,1:오른쪽아래,2:왼쪽아래,3:오른쪽 위
di = [-1,1,1,-1]
dj = [1,1,-1,-1]
#무조건 오른쪽 위로 올라가는 걸로 시작하기(같은거 반복 줄이려고)
def eat_desert(i,j,dir,move,visited):
    global max_eat_desert, start_i, start_j
    if dir == 3:
        if i == start_i and j == start_j: # 출발 위치로 돌아 온 경우
            max_eat_desert = max(max_eat_desert,move)
            return
        #아직 못 돌아왔으면 현재 방향대로 한칸 더 가
        ni, nj = i + di[dir], j + dj[dir]
        if 0<=ni<N and 0<=nj<N and cafe[ni][nj] not in visited:
            eat_desert(ni, nj, dir, move+1, visited+[cafe[ni][nj]])
        return

    ni, nj = i + di[dir], j + dj[dir] #위치 이동
    if 0<=ni<N and 0<=nj<N and cafe[ni][nj] not in visited: #정상 위치에 있고, 들린곳중 종류 수가 같은게 없으면
        eat_desert(ni, nj, dir, move+1, visited+[cafe[ni][nj]]) #현재 방향으로 한칸 가기
        eat_desert(ni, nj, dir+1, move+1, visited+[cafe[ni][nj]]) #현재 방향으로 한칸 가고 방향 전환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int,input().split())) for _ in range(N)]
    max_eat_desert = -1 #최대 먹을 수 있는 디저트 수
    for start_i in range(N):
        for start_j in range(N):
            if start_i != 0 and start_j != N-1: #오른쪽 위로 가자마자 막힐 곳들은 빼버리기
                eat_desert(start_i,start_j,0,0,[])
    print(f'#{tc} {max_eat_desert}')
```


###  실패했던 첫 시도
진짜 맞춘줄 알았는데... 5번 케이스부터 쭉 답보다 큰 수가 나옴...
```python
def eat_desert(start_i,start_j,i,j,move,visited):
    global max_eat_desert
    for di, dj in [(1,-1),(1,1),(-1,1),(-1,-1)]:
        ni,nj = i+di, j+dj
        if ni == start_i and nj == start_j and move>1 and cafe[ni][nj] not in visited:
            if max_eat_desert < move+1:
                max_eat_desert = move+1
            return
        if 0<=ni<N and 0<=nj<N and cafe[ni][nj] not in visited:
            if not(ni==start_i and nj==start_j and move == 1):
                eat_desert(start_i,start_j,ni,nj,move+1,visited+[cafe[ni][nj]])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int,input().split())) for _ in range(N)]
    max_eat_desert = -1 #최대 먹을 수 있는 디저트 수
    for start_i in range(N):
        for start_j in range(N):
            if (start_i,start_j) not in [(0,0),(0,N-1),(N-1,0),(N-1,N-1)]:
                eat_desert(start_i,start_j,start_i,start_j,0,[])
    print(f'#{tc} {max_eat_desert}')
```
아오... 문제좀 잘 읽자!
"사각형 방향으로 움직이고 `사각형 모양을 그리며` 출발한 카페로 돌아와야 한다."

사각으로 안가고 요리조리 가능한 모든 곳을 가고 있었음