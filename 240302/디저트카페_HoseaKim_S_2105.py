# 디저트 카페 swea 2105
def f():
    global max_cnt
    for i in range(1, n-1):
        for j in range(1, n-1):

            # visited 길이 = 모든 디저트 종류 = 1 ~ 100
            v = [0] * 101
            for d in range(2, 4):      # ← ↑
                if v[arr[i + dx[d]][j + dy[d]]] == 0:
                    v[arr[i + dx[d]][j + dy[d]]] = 1
            if sum(v) == 2:
                k = 0
                while i+k < n-1 and j+k < n-1:      # ↘
                    Ri, Rj = i+k, j+k
                    for d in range(2):                  # → ↓
                        if v[arr[Ri + dx[d]][Rj + dy[d]]] == 0:
                            v[arr[Ri + dx[d]][Rj + dy[d]]] = 1
                        else:
                            break
                    else:
                        k += 1
                        continue
                    break
                if max_cnt < k:
                    max_cnt = k
                    if max_cnt == n - 1 - i:
                        return

            v = [0] * 101
            for d in (0, 3):      # ↑ →
                if v[arr[i + dx[d]][j + dy[d]]] == 0:
                    v[arr[i + dx[d]][j + dy[d]]] = 1
            if sum(v) == 2:
                k = 0
                while i+k < n-1 and j-k >= 1:           # ↙
                    Li, Lj = i+k, j-k
                    for d in range(1, 3):                  # ↓ ←
                        if v[arr[Li + dx[d]][Lj + dy[d]]] == 0:
                            v[arr[Li + dx[d]][Lj + dy[d]]] = 1
                        else:
                            break
                    else:
                        k += 1
                        continue
                    break
                if max_cnt < k:
                    max_cnt = k
                    if max_cnt == n - 1 - i:
                        return


T = int(input())
for case in range(1, T+1):
    # 한 변의 길이 (4 ~ 20)
    n = int(input())
    # 디저트 종류는 1 ~ 100
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    # 최대 stack = 최대 디저트 종류 = n-1 * 2
    stack = [0] * (n - 1) * 2
    top = -1

    max_cnt = 0
    ans = -1
    f()

    if max_cnt:
        ans = (max_cnt * 2) + 2

    print(f'#{case}', ans)

'''
좌우 대각 최대길이만큼 넓히고 (가다가 디저트 종류 겹치면 break)
다시 만나는 지점까지 좁히기
if 다 좁히면 cnt = sum(부모 대각선) * 2 - 4
    -> 다음 시작점으로 가서 처음부터 다시 동작
    (넓히는 길이가 최대 길이보다 작거나 같으면 pass)
else 못 좁히면 부모 대각선 최대 길이 1 감소
'''