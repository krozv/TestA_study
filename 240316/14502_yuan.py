from collections import deque
from copy import deepcopy

import sys
input = sys.stdin.readline

def f2(arr):
    global max_v
    cnt = 0
    for i in range(N):
        for j in range(M):
           if arr[i][j] ==0:
               cnt+=1

    max_v = max(cnt,max_v)
    return

#
def f(map): #바이러스 퍼트리기
    arr = deepcopy(map)
    # 중복없이 가야함
    # for i in arr:
    #     print(i)
    # print()
    visit = [[0]*M for _ in range(N)]
    q= deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i,j))
                visit[i][j] = 1
    while q:
        #바이러스 좌표
        x,y = q.popleft()
        for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dir[0], y+dir[1]
            if 0<= nx < N and 0<= ny < M and not visit[nx][ny]:
                if arr[nx][ny] == 0: # 상하좌우 중 빈칸
                    q.append((nx,ny))
                    visit[nx][ny] = 1 # 방문표시
                    arr[nx][ny] = 2  # 바이러스 먹이기
    # for i in arr:
    #     print(i)
    # print()
    # return arr
    return f2(arr)


# 세로, 가로
N, M = map(int, input().split())
map = [list(map(int,input().split()))for _ in range(N)]

max_v = 0
# 빈칸있는 좌표
wall = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            wall.append((i,j))

w = len(wall) # w는 벽 개수
# print(wall)
for a in range(w):
    for b in range(a+1,w):
        for c in range(b+1,w):
            x1,y1 = wall[a]
            x2,y2 = wall[b]
            x3,y3 = wall[c]
            map[x1][y1] = 1
            map[x2][y2] = 1
            map[x3][y3] = 1
            # 좌표 3개 0으로 만든다음에 바이러스 퍼트리기
            # print((x1,y1),(x2,y2),(x3,y3))
            # for i in map:
            #     print(i)
            # print()
            f(map)
            # 원상복구
            map[x1][y1] = 0
            map[x2][y2] = 0
            map[x3][y3] = 0


print(max_v)