import sys
from collections import deque

m, n, height = map(int, input().split())
tomato = []
start = deque()
result = 0
flag = False

for h in range(height):
    tmp = []
    for y in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for x in range(m):
            if tmp[y][x] == 1:
                start.append((h, x, y))
    tomato.append(tmp)

while start:
    h, x, y = start.popleft()
    for d in [0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]:
        mh = h + d[0]
        mx = x + d[1]
        my = y + d[2]

        if 0 <= mx < m and 0 <= my < n and 0 <= mh < height and tomato[mh][my][mx] == 0:
            start.append((mh, mx, my))
            tomato[mh][my][mx] = tomato[h][y][x] + 1

for h in tomato:
    for t in h:
        if 0 in t:
            flag = True
        result = max(result, max(t))
if flag:
    print(-1)
else:
    print(result-1)