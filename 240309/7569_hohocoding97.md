# 7569. 토마토
python3:3508ms, pypy3:580ms
```python
#1:익은 토마토, 0:안 익은 토마토, -1:토마토없음
import sys, collections
input = sys.stdin.readline
M,N,H = map(int,input().split()) #각각 가로,세로,높이

#인덱싱할때 높이, 가로, 세로 순
box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

tomato = 0
tomato_q = collections.deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 1:  #익은 토마토
                tomato_q.append((k,i,j))
            elif box[k][i][j] == 0: #안익은 토마토
                tomato += 1

if tomato == 0: #안익은 토마토 없을 ㄸ
    print(0)
else:
    cnt = 0
    while tomato_q:
        k, i, j = tomato_q.popleft() #익은 토마토 위치
        for dk,di,dj in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]: #6방향 순회
            nk, ni, nj = k+dk, i+di, j+dj
            if 0<=nk<H and 0<=ni<N and 0<=nj<M and box[nk][ni][nj] == 0: #익은 토마토 근처에 안익은 토마토 있는 경우
                box[nk][ni][nj] = time = box[k][i][j] + 1
                tomato_q.append((nk,ni,nj))
                cnt += 1
    
    if cnt == tomato:
        print(time-1)
    else:
        print(-1)
```