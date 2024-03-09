# 뱀
def bfs(i, j, d, t):
    """
    t: 현재 시간
    d: 현재 방향
    """
    q = deque()
    q.append([i, j, d])
    t = 0
    while q:
        snake.append([q[-1][0], q[-1][1]])
        delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        d = q[-1][-1]
        if t in change:
            if change[t] == 'D':
                d = (d+1) % 4
            else:
                d = (d+3) % 4
        ni = q[-1][0] + delta[d][0]
        nj = q[-1][1] + delta[d][1]
        if 0<=ni<N and 0<=nj<N and [ni, nj] not in snake:
            if arr[ni][nj] == 0:
                snake.popleft()
                q.append([ni, nj, d])
            # 사과가 있다면
            elif arr[ni][nj] == 1:
                q.append([ni, nj, d])
                arr[ni][nj] = 0
        q.popleft()
        t += 1
    return t

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1][j-1] = 1
L = int(sys.stdin.readline())
change = {}
for _ in range(L):
    X, C = sys.stdin.readline().split()
    X = int(X)
    change[X] = C
snake = deque()
print(bfs(0, 0, 1, 0))
