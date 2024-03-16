# 14891. 톱니바퀴

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
arr = [deque(map(int, list(input().strip()))) for _ in range(4)]
cnt = int(input())

for _ in range(cnt):
    # 1: 시계 방향, -1: 반시계 방향
    curr, d = map(int, input().split())
    curr -= 1
    temp = curr
    rot = [0] * 4
    rot[curr] = d
    # 오른쪽 방향
    while rot[curr] and curr < 3:
        if arr[curr][2] != arr[curr+1][6]:
            rot[curr+1] = -rot[curr]
        curr += 1
    # 왼쪽 방향
    curr = temp
    while rot[curr] and 0 < curr:
        if arr[curr][6] != arr[curr-1][2]:
            rot[curr-1] = -rot[curr]
        curr -= 1
    # 회전
    for i in range(4):
        # 시계 방향으로 회전하는 톱니바퀴라면
        if rot[i] == 1:
            arr[i].appendleft(arr[i].pop())
        # 반시계 방향 회전
        elif rot[i] == -1:
            arr[i].append(arr[i].popleft())

# 점수 계산
point = 0
# N극: 0, S극: 1
for i in range(4):
    if arr[i][0] == 1:
        point += 2 ** i
print(point)