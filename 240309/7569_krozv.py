"""
토마토
6방향, 대각선 불가
혼자 저절로 익는 경우는 없음
토마토가 모두 익는지, 최소 일수 구하기
dfs?
"""
def bfs():
  # arr == 1인 토마토 좌표 수집
  q = deque()
  visited = [[[0 for _ in range(M)]for _ in range(N)] for _ in range(H)]
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if arr[i][j][k] == 1:
          q.append([i, j, k, 0])
          visited[i][j][k] = 1
  if len(q) == 0:
    return 0
  max_cnt = 0
  while q:
    delta = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
    for d in delta:
      ni = q[0][0] + d[0]
      nj = q[0][1] + d[1]
      nk = q[0][2] + d[2]
      cnt = q[0][3] + 1
      # 범위 안이고, 방문한적 없으며, 토마토가 0이어야함
      if 0<=ni<H and 0<=nj<N and 0<=nk<M and visited[ni][nj][nk]==0 and arr[ni][nj][nk]==0:
        visited[ni][nj][nk] = 1
        arr[ni][nj][nk] = 1
        if max_cnt < cnt:
          max_cnt = cnt
        q.append([ni, nj, nk, cnt])
    q.popleft()
  return max_cnt



import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = []
for _ in range(H):
  f = [list(map(int, input().split())) for _ in range(N)]
  arr.append(f)

date = bfs()

tomato = True
for i in range(H):
  if tomato:
    for j in range(N):
      for k in range(M):
        if arr[i][j][k] == 0:
          tomato = False
          break
if tomato:
  print(date)
else:
  print(-1)