# 장훈이의 높은 선반 SWEA 1486
def combination(i, ss):
    global min_ss
    if ss >= b:
        if min_ss > ss:
            min_ss = ss
        return
    if i == n:
        return
    combination(i+1, ss + h[i])
    combination(i+1, ss)


T = int(input())
for case in range(1, T+1):
    # 점원의 수, 선반의 높이
    n, b = map(int, input().split())
    # 점원들의 키
    h = list(map(int, input().split()))

    min_ss = 10**9
    combination(0, 0)

    print(f'#{case}', min_ss - b)
