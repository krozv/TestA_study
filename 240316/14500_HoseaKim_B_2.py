# 백준 14500 테트로미노 (골드4)
# dfs 풀이
# python3 : 36,420 KB / 224 ms
# pypy3 : 113,872 KB / 200 ms
n, m = map(int, input().split())    # 4 ~ 500
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, cnt, d, ss):
    global ans
    if ans >= ss + max_v * (3 - cnt):
        return
    if cnt == 3:
        if ans < ss:
            ans = ss
        return
    for dir in range(-1, 2, 1):
        nx, ny = x + dx[(d+dir)%4], y + dy[(d+dir)%4]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx, ny, cnt+1, (d+dir)%4, ss+arr[nx][ny])
    if cnt == 2:
        global i, j
        if x == i + 2:
            for dj in [-1, 1]:
                ny = j + dj
                if 0 <= ny < m:
                    for di in range(2):
                        nx = i + di
                        if 0 <= nx < n:
                            dfs(nx, ny, cnt+1, d, ss+arr[nx][ny])
        elif y == j + 2:
            for di in [-1, 1]:
                nx = i + di
                if 0 <= nx < n:
                    for dj in range(2):
                        ny = j + dj
                        if 0 <= ny < m:
                            dfs(nx, ny, cnt+1, d, ss+arr[nx][ny])

    return

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

max_v = max(map(max, arr))
ans = 0

for i in range(n):
    for j in range(m):
        dfs(i, j, 0, 0, arr[i][j])
        dfs(i, j, 0, 1, arr[i][j])

print(ans)