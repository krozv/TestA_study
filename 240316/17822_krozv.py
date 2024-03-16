import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, T = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    # x의 배수인 원판을 d방향으로 k칸 회전
    # d: 0 시계방향 1 반시계방향
    x, d, k = map(int, input().split())

    # x의 배수인 원판만 선택
    for i in range(x-1, N, x):
        # d 방향으로 k칸 회전
        for _ in range(k):
            # 시계 방향
            if d == 0:
                arr[i].appendleft(arr[i].pop())
            # 반시계 방향
            else:
                arr[i].append(arr[i].popleft())

    # 회전 종료 후 점수 계산
    s = 0
    num = 0
    deleted = False
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                temp = arr[i][j]
                q = deque()
                q.append([i, j])
                while q:
                    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ni = q[0][0] + d[0]
                        nj = (q[0][1] + d[1] + M) % M
                        if 0<=ni<N and temp == arr[ni][nj]:
                            arr[ni][nj] = 0
                            arr[i][j] = 0
                            q.append([ni, nj])
                            deleted = True
                    q.popleft()
        s += sum(arr[i])
        num += (M - arr[i].count(0))

    # 평균 계산 후 숫자 수정
    if not deleted and num:
        average = s / num
        for i in range(N):
            for j in range(M):
                if arr[i][j] and arr[i][j] > average:
                    arr[i][j] -= 1
                elif arr[i][j] and arr[i][j] < average:
                    arr[i][j] += 1

ss = 0
for i in range(N):
    ss += sum(arr[i])
print(ss)

