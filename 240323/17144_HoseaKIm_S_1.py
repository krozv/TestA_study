# 백준 17144 미세먼지 안녕! (골드4) 풀이1 데크 사용 (시간초과)
import sys
from collections import deque
input = sys.stdin.readline

# r, c : 6~50 / t : 1~1000
r, c, t = map(int, input().split())
# -1 ~ 1000
arr = [list(map(int, input().split())) for _ in range(r)]

for i in range(2, r-2):
    if arr[i][0] == -1:
        start = i
        break

dq = deque()
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            dq.append([i, j])

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

time = 0
while dq and time < t:
    time += 1
    copied_arr = [[] for _ in range(r)]
    for i in range(r):
        copied_arr[i] = arr[i][:]
    # 먼지 확산
    init_len = len(dq)
    for _ in range(init_len):
        i, j = dq.popleft()
        cnt = 0
        if arr[i][j] >= 5:
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                    arr[ni][nj] += copied_arr[i][j] // 5
                    if arr[ni][nj] and [ni, nj] not in dq:
                        dq.append([ni, nj])
                    cnt += 1
        arr[i][j] -= (copied_arr[i][j] // 5) * cnt
        dq.append([i, j])
    # 공기청정기 동작
    for k in [0, 1]:
        i, j = start+k - 1+2*k, 0
        d = 3 - 2*k
        while i != start+k or j != 1:
            ni, nj = i + dx[d], j + dy[d]
            if (
                    0 <= ni < r and 0 <= nj < c and
                    ni != start+k + 1-2*k and
                    (arr[i][j] != 0 or arr[ni][nj] != 0)
            ):
                arr[i][j] = arr[ni][nj]
                if [ni, nj] in dq:
                    dq.remove([ni, nj])
                if arr[i][j] and [i, j] not in dq:
                    dq.append([i, j])
                elif arr[i][j] == 0 and [i, j] in dq:
                    dq.remove([i, j])
                i, j = ni, nj
            else:
                d = (d + 1 - 2*k) % 4
        arr[i][j] = 0

ans = sum(map(sum, arr)) + 2
print(ans)
