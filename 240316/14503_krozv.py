# 14503. 로봇 청소기
"""
방 N * M
1 * 1 크기의 정사각형 칸
(r, c) 좌표로 나타냄
(N-1, M-1)
1. 청소 안되어있을 경우 -> 청소
2. 4칸 중 청소되지 않은 빈칸 없는 경우 -> 현재 방향에서 후진 1칸
2-1. 후진 불가일 경우 작동 멈춤
3. 4칸 중 청소되지 않은 빈칸 있을 경우 -> 반시계 방향으로 회전
"""
def f(x, y, d):
    global number_of_room
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 현재 칸이 청소되지 않았을 경우
    if arr[x][y] == 0:
        # 청소한다.
        arr[x][y] = 2
        number_of_room += 1
    # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    cnt = 0
    while cnt < 4:
        cnt += 1
        d = (d-1) % 4
        ni = x + delta[d][0]
        nj = y + delta[d][1]
        # 90도 돌아간 방향이 청소되지 않은 빈 칸인 경우 한 칸 전진
        if arr[ni][nj] == 0:
            f(ni, nj, d)
            break
        # 아닐 경우 다시 처음으로 돌아감
    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우 -> 한 칸 후진
    else:
        ni = x - delta[d][0]
        nj = y - delta[d][1]
        if arr[ni][nj] != 1:
            f(ni, nj, d)
        else:
            return

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # r, c 현재 로봇청소기 좌표, d: 로봇 청소기가 바라보는 방향
arr = [list(map(int, input().split())) for _ in range(N)]   # 1: 벽, 0: 청소되지않음

number_of_room = 0
f(r, c, d)
print(number_of_room)