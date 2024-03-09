from collections import deque

n = int(input())
k = int(input())

arr= [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
l = int(input())

#시간 리스트
turn = []
for _ in range(l):
    t, d = map(str, input().split())
    turn.append((int(t), d))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
nd, hx, hy = 0, 0, 0
time, i = 0, 0
q = deque()
q.append((hx, hy))

while True:
    hx = hx + dx[nd]
    hy = hy + dy[nd]
    time += 1
    if hx < 0 or hx >= n or hy < 0 or hy >= n or (hx, hy) in q:
        break
    
    q.append((hx, hy))
    
    if arr[hx][hy] == 0:
        q.popleft()
    else:
        # 사과만나면 사과 0으로 바꿔줌
        arr[hx][hy] = 0


    #시간 다되면 방향 바꾸기
    if time == turn[i][0]:
        if turn[i][1] == 'L':
            nd = (nd - 1) % 4
        else:
            nd = (nd + 1) % 4
        # 다음 turn 으로 넘어가기
        if i + 1 < len(turn):
            i += 1

print(time)



# dir=[(0,1),(1,0),(0,-1),(-1,0)]
#
# #현재위치/ 꼬리위치/방향/시간/정보 변환횟수
# def dfs( si,sj, k, t, i):
#
#     cnt = 0
#     while 0<= ni< N and 0<= nj<N and not visit[ni][nj] and (t+cnt) < int(dir_change[i][0]):
#         ni, nj = ni + dir[k][0], nj + dir[k][1]
#         cnt += 1  # 이동 횟수 기록
#         if not (0 <= ni < N and 0 <= nj < N and not visit[ni][nj]):
#             break
#
#         #이동
#         si, sj = ni, nj
#         visit[si][sj] = 1
#         tail.append((si, sj))
#         #사과 없으면 이동기록에서 pop
#         if [si,sj] not in apple:
#             ei, ej = tail.pop(0)
#             visit[ei][ej] = 0  # visit 취소해주기
#         else:
#             #사과있으면 꼬리 유지 - 사과만 빼주기
#             apple.remove([si,sj])
#
#     # 막혀서 빠져나온경우
#     if not( 0<= ni< N and 0<= nj<N and not visit[ni][nj]):
#         break
#
#     # t+cnt >= dirchange[i][0]일떄 방향바꿔서 이동,
#     else:
#         if dir_change[i][1] == 'L':
#             k = (k-1+4)%4
#         else:
#             k = (k+1) % 4
#
#         # 현재위치/방향/시간 / 정보 변환횟수
#         dfs(si,sj,k,cnt+t+1,i+1)
#
#
# N = int(input())
# k= int(input()) # 사과개수
#
# #사과 정보 [[3,4],[2,5] ... ]
# apple = [list(map(int, input().split())) for _ in range(k)]
#
# l = int(input()) # 정보 변환횟수
# # 방향정보 [[3,D], [15,L], ...] : 3초 뒤에 4초부터 회전,
# dir_change = [list(input().split()) for _ in range(l)]
#
# visit = [[0]*N for _ in range(N)]
# visit[0][0] =1
# tail = [(0,0)]
# #현재위치/방향/시간 / 정보 변환횟수
# dfs(0,0, 0, 0,0)
#
