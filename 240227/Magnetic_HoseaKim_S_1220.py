# Magnetic
from collections import deque

T = 10
for case in range(1, T+1):
    n = int(input())    # = 100
    # 1 : n극 ↓, 2 : s극 ↑
    arr = [list(map(int, input().split())) for _ in range(n)]

    mag_list = [deque() * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            # 1 : n극 ↓, -1 : s극 ↑
            if arr[n-1-i][j] == 1:
                mag_list[j].append(n-1-i)
            if arr[i][j] == 2:
                arr[i][j] = -1
                mag_list[j].append(i)

    cnt = 0
    for j in range(n):
        while mag_list[j]:
            i = mag_list[j].popleft()
            d = arr[i][j]
            if i+d < 0 or i+d >= n:
                continue

            if abs(arr[i][j]) == 2:
                continue

            elif abs(arr[i][j]) == 1:
                if arr[i][j] == -arr[i+d][j]:
                    arr[i][j] += d
                    arr[i+d][j] -= d
                    cnt += 1
                elif arr[i][j] * 2 == -arr[i+d][j]:
                    arr[i][j] += d
                    cnt += 1
                elif arr[i][j] * 2 == arr[i+d][j]:
                    arr[i][j] += d
                else:
                    arr[i][j], arr[i+d][j] = 0, d
                    mag_list[j].append(i+d)

    print(f'#{case}', cnt)
