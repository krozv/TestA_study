from collections import deque
import copy

def f1(x,d,k,q): # row 판별수, 방향, 회전 수
    for row in range(N): # row 가 행 인덱스
        if (row+1) % x == 0: #행이 x배수
            # print(row)
            if d==0: # 시계방향
                for _ in range(k):
                    c=q[row].pop()
                    q[row].appendleft(c)

            else:# 반대방향
                for _ in range(k):
                    c=q[row].popleft()
                    q[row].append(c)

    return q


def f2(rot_arr):
    new_arr = copy.deepcopy(rot_arr)

    # 나중에 평균구해야함
    total = cnt = 0
    for i in range(N):
        for j in range(M):
            if rot_arr[i][j]: #0 아닐떄 수 더하기
                total+= rot_arr[i][j]
                cnt+=1

            # 중복허용해서 모든 좌표 순회하면서 인접수 찾음
            for k in range(4):
                ni, nj = i+dir[k][0], j +dir[k][1]

                if 0<= ni < N and 0<= nj <M:

                    # 같은지 확인
                    if rot_arr[ni][nj] == rot_arr[i][j]:
                        new_arr[i][j] = 0
                        new_arr[ni][nj] = 0
    # 순회 다 끝나도 한 행의 양쪽 끝도 체크ㅐ주기
    for i in range(N):
        if rot_arr[i][0] == rot_arr[i][M-1]:
            new_arr[i][0] = 0
            new_arr[i][M-1] = 0

    #만약 인접수가 한개도 없었을 경우
    if new_arr == rot_arr and cnt!=0:
        avg= total/ cnt

        for i in range(N):
            for j in range(M):
                if new_arr[i][j] > avg:
                    new_arr[i][j] -=1
                elif new_arr[i][j] and new_arr[i][j] < avg:
                    new_arr[i][j] +=1

    return new_arr



dir = [(1,0),(-1,0),(0,1),(0,-1)]

N, M , T = map(int, input().split())
arr = [ list(map(int,input().split()))for _ in range(N)]

rotation = [ list(map(int,input().split())) for _ in range(T)]

q=deque([])
for i in arr:
    q.append(deque(i))

i = 0 # 첫번째 rotation
while True:
    rot_arr = f1(rotation[i][0],rotation[i][1],rotation[i][2],q) # 회전
    new_arr = f2(rot_arr) # 인접수 없애는 함수

    if i == T-1:
        break
    else:
        i+=1
        q = new_arr

res = 0
for i in range(N):
    for j in range(M):
       res += new_arr[i][j]

print(res)