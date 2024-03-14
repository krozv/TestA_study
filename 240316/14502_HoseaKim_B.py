# 백준 14502 연구소 (골드4)
from collections import deque


def combination(r, c, cnt):
    global ans
    if cnt == 3:
        temp = bfs(safe)
        if ans < temp:
            ans = temp
        return
    i, j = r, c
    while i != n:
        while j != m:
            if arr[i][j] == 0:
                arr[i][j] = 1
                combination(i, j, cnt + 1)
                arr[i][j] = 0
            j += 1
        i += 1
        j = 0


def bfs(cnt):
    dq = deque(q)
    new_arr = [0] * n
    for i in range(n):
        new_arr[i] = arr[i][:]
    while dq:
        i, j = dq.popleft()
        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < n and 0 <= nj < m:
                if new_arr[ni][nj] == 0:
                    new_arr[ni][nj] = 2
                    cnt -= 1
                    dq.append([ni, nj])
    return cnt


n, m = map(int, input().split())    # 3~8
# 빈칸0 벽1 바이러스2(2~10)
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = []
safe = -3
ans = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            safe += 1
        elif arr[x][y] == 2:
            q.append([x, y])

combination(0, 0, 0)

# print(safe, *q)
print(ans)
