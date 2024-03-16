"""
2주변의 0개수를 구해
0개수가 <= 3 -> 벽 세움
0개수가 > 3 -> 바이러스 퍼져 위에 다시 반복
완전탐색이면 모든 경우의 수 탐색해봐야하나?
"""
def bfs():
    global max_area
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque()
    q.extend(virus)
    visited = []
    area = 0
    while q:
        x = q[0][0]
        y = q[0][1]
        for d in delta:
            ni = x + d[0]
            nj = y + d[1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and [ni, nj] not in visited:
                visited.append([ni, nj])
                q.append([ni, nj])
        q.popleft()
        # 안전 구역 개수 = area
        area = initial_area-len(visited)
        if max_area > area:
            break

    if max_area < area:
        max_area = area
        return


import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

wall = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            wall.append((i, j))
        elif arr[i][j] == 2:
            virus.append([i, j])
initial_area = len(wall)-3  # 초기 0 개수
wall_comb = list(combinations(wall, 3))
max_area = 0
for comb in wall_comb:
    # 벽 세우기
    for x, y in comb:
        arr[x][y] = 1
    # bfs 시작
    bfs()
    # 벽 허물기
    for x, y in comb:
        arr[x][y] = 0
print(max_area)
