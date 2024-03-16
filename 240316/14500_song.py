# 14500_테트로미노
'''
https://www.acmicpc.net/problem/14500
'''
def figure1(x, y, s, c):
    global result, verify
    if c == 4 or result >= s + verify*(4-c):
        if s > result:
            result = s
        return

    for d in range(4):
        mx = x + dx[d]
        my = y + dy[d]

        if 0 <= mx < m and 0 <= my < n and not visited[my][mx]:
            visited[my][mx] = 1
            figure1(mx, my, s+paper[my][mx], c+1)
            visited[my][mx] = 0

def figure2(x, y, d, c):
    global result
    if c == 4:
        return

    cnt = paper[y][x]
    for i in range(3):
        direction = (i+d) % 4
        mx = x + dx[direction]
        my = y + dy[direction]
        if mx < 0 or mx >= m or my < 0 or my >= n:
            cnt = 0
            break
        else:
            cnt += paper[my][mx]

    if cnt > result:
        result = cnt

    figure2(x, y, d+1, c+1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

paper = []
visited = [[0]*m for _ in range(n)]

result = 0
verify = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    paper.append(tmp)
    if max(tmp) > verify:
        verify = max(tmp)

for y in range(n):
    for x in range(m):
        # visited를 여기서 생성하면 시간초과
        # visited = [[0]*m for _ in range(n)]

        visited[y][x] = 1
        figure1(x, y, paper[y][x], 1)
        visited[y][x] = 0

        figure2(x, y, 0, 0)

print(result)