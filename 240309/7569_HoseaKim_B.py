# 백준 7569 토마토
# https://www.acmicpc.net/problem/7569
from collections import deque

# 가로 m(2~100) 세로 n(2~100) 높이 h(1~100)
m, n, h = map(int, input().split())
# 1 익토 / 0 안익토 / -1 없토
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

# 익은 토마토 찾기. cnt = 익토 개수
cnt = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                q.append([z, x, y])
            elif arr[z][x][y] == 0:
                cnt += 1

# 더이상 익힐 수 없거나 (q가 없거나)
# 남은 안익토가 없으면 (cnt가 없으면) 종료
day = 0
while q and cnt:
    # 하루마다 익은 토마토를 q에서 꺼내 주변 익히기
    day += 1
    q_len = len(q)
    for _ in range(q_len):
        z, x, y = q.popleft()
        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = 1
                    q.append([nz, nx, ny])
                    # 주변 익힐 때마다 안익토 개수 -1
                    cnt -= 1

if cnt:
    print(-1)
else:
    print(day)