# 백준 17144 미세먼지 안녕! (골드4) 풀이2 스왑 사용
# Python: 시간초과
# PyPy: 111,488 KB / 317 ms
import sys
input = sys.stdin.readline

# r, c : 6~50 / t : 1~1000
r, c, t = map(int, input().split())
# -1 ~ 1000
arr = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 찾기
for i in range(2, r-2):
    if arr[i][0] == -1:
        start = i
        break

# 시뮬레이션 시작
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
time = 0
while time < t:
    time += 1
    # 먼지 확산
    new_arr = [[] for _ in range(r)]
    for i in range(r):
        new_arr[i] = arr[i][:]
    for i in range(r):
        for j in range(c):
            if arr[i][j] >= 5:
                diffusion = new_arr[i][j] // 5
                cnt = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                        arr[ni][nj] += diffusion
                        cnt += 1
                arr[i][j] -= diffusion * cnt
    # 공기청정기 동작
    for k in [0, 1]:
        i, j = start+k, 1
        d = 0
        temp = 0
        while i != start+k or j != 0:
            arr[i][j], temp = temp, arr[i][j]
            ni, nj = i + dx[d], j + dy[d]
            if not (0 <= ni < r and 0 <= nj < c):
                d = (d - 1 + 2*k) % 4
                ni, nj = i + dx[d], j + dy[d]
            i, j = ni, nj

ans = sum(map(sum, arr)) + 2
print(ans)
