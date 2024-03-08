# 백준 3190 뱀
# https://www.acmicpc.net/problem/3190
from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]

# 사과, 위치로!
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

L = int(input())
# x초 이후 왼쪽 L 오른쪽 D
turn = [list(input().split()) for _ in range(L)]
turn_idx = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

# 시작점
i, j = 0, 0

# 데크와 arr에 꼬리 정보 저장하기
q = deque([[0, 0]])
arr[0][0] = 2

# 시작 시간
t = 0

while True:

    # 한 칸 이동
    t += 1
    i += dx[d]
    j += dy[d]

    # 벽 만나면 종료
    if i < 0 or i >= n or j < 0 or j >= n:
        break

    # 꼬리 만나면 종료
    if arr[i][j] == 2:
        break

    # 사과 없으면 꼬리 길이 -1
    elif arr[i][j] == 0:
        temp = q.popleft()
        arr[temp[0]][temp[1]] = 0

    # 현재 위치에 꼬리 +1
    q.append([i, j])
    arr[i][j] = 2

    if turn_idx < L and t == int(turn[turn_idx][0]):
        if turn[turn_idx][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        turn_idx += 1

print(t)