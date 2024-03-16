# ㅗ모양을 제외한 경로 탐색
def f(x, y, n, s):
    global path
    global max_val
    if [x, y] not in path:
        path.append([x, y])
        s += arr[x][y]

    delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    # 4칸 채우면 최댓값 계산
    if n == 3:
        max_val = max(max_val, s)
        return
    # backtracking
    if max_val - s >= 1000 * (3 - n):
        return

    for i in range(4):
        ni = x + delta[i][0]
        nj = y + delta[i][1]
        if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in path:
            f(ni, nj, n+1, s)
            path.pop()

# ㅗ모양 경로 탐색
def f2(x, y):
    global max_val
    delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for i in range(4):
        path = [[x, y]]
        s = arr[x][y]
        d = i
        n = 0
        while True:
            ni = x + delta[d][0]
            nj = y + delta[d][1]
            if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in path:
                path.append([ni, nj])
                s += arr[ni][nj]
                d = (d + 1) % 4
                n += 1
            else:
                break

            # 4칸 채우면 최대값 계산
            if n == 3:
                max_val = max(max_val, s)
                break
            # backtracking
            if max_val - s >= 1000 * (3 - n):
                break

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())  # 4<=N,M<=500
arr = [list(map(int, input().split())) for _ in range(N)]
max_val = 0

for i in range(N):
    for j in range(M):
        path = []
        f(i, j, 0, 0)
        f2(i, j)

print(max_val)