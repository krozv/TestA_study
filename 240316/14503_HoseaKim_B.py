# 백준 14503 로봇 청소기 (골드5)
n, m = map(int, input().split())
i, j, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# d -> 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소X = 0, 벽 = 1 청소O = 2
ans = 0
while True:
    # 청소X면 청소O로
    if arr[i][j] == 0:
        arr[i][j] = 2
        ans += 1
    # 반시게 90도로 탐색 (다 하면 제자리로 옴)
    d = dir
    for _ in range(4):
        d = (d - 1) % 4
        ni = i + dx[d]
        nj = j + dy[d]
        if 0 <= ni < n and 0 <= nj < m:
            # 청소X 발견하면 이동
            if arr[ni][nj] == 0:
                i, j = ni, nj
                dir = d
                break
    else:
        # 청소X를 발견 못하면 뒤로 후진
        ni = i - dx[d]
        nj = j - dy[d]
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] != 1:
                i, j = ni, nj
            # 후진 못하면 끝
            else:
                break
print(ans)