# 백준 14891 톱니바퀴 (골드5)
arr = [list(map(int, input())) for _ in range(4)]
left = [6] * 4
right = [2] * 4
k = int(input())
for _ in range(k):
    i, t = map(int, input().split())
    turn = [0] * 4
    turn[i - 1] = t
    L = R = i - 1
    while L - 1 >= 0 and arr[L - 1][right[L - 1]] != arr[L][left[L]]:
        L -= 1
        turn[L] = -turn[L+1]
    while R + 1 < 4 and arr[R + 1][left[R + 1]] != arr[R][right[R]]:
        R += 1
        turn[R] = -turn[R-1]
    for x in range(L, R+1):
        left[x] = (left[x] - turn[x]) % 8
        right[x] = (right[x] - turn[x]) % 8

ans = 0
for x in range(4):
    if arr[x][(left[x] + 2) % 8] == 1:
        ans += 2 ** x

print(ans)
