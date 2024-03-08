# 3190. 뱀
### 코드
68ms
```python
import sys, collections
input = sys.stdin.readline

di = [0,1,0,-1]
dj = [1,0,-1,0]

N = int(input()) #보드의 크기
K = int(input()) #사과 개수
game_map = [[0]*N for _ in range(N)] #N*N크기의 맵 만들기
for _ in range(K):
    r, c = map(int,input().split()) #사과 존재하는 열과 행 의미
    game_map[r-1][c-1] = 1 #사과 있는 위치를 1로 지정
L = int(input()) #방향전환 횟수
moves = collections.deque()
for _ in range(L):
    t, change_dir = input().split()
    moves.append((int(t),change_dir)) #방향변경 정보 moves에 넣기

now_time = 0
snake_pos = collections.deque()
snake_pos.append((0,0))
head_i, head_j = 0, 0 #머리의 위치
dir = 0
while True:
    if moves and now_time == moves[0][0]: #움직일 게 남아 있고 머리를 움직여야 할 시간이면??
        change = moves.popleft()[1] #변경해야 할 방향
        if change == 'D': dir = (dir+1)%4   #D : 우회전
        else: dir = (dir+3)%4               #L : 좌회전
    head_i, head_j = head_i+di[dir], head_j + dj[dir] #머리 이동
    now_time += 1 #시간 증가
    if not(0<=head_i<N) or not(0<=head_j<N) or (head_i, head_j) in snake_pos: #맵 벗어나거나 몸에 부딪힌 경우
        break
    elif game_map[head_i][head_j] == 1: #머리 위치에 사과 있으면
        game_map[head_i][head_j] = 0 #사과 먹어 없애기
        snake_pos.append((head_i, head_j))
    else:
        snake_pos.popleft() #꼬리 빼기
        snake_pos.append((head_i, head_j))
print(now_time)
```