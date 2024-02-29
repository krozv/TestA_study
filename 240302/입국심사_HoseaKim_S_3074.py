# 입국심사 swea 3074
T = int(input())
for case in range(1, T+1):
    # n개의 심사대, m명의 입국심사
    n, m = map(int, input().split())
    # 심사대 별 소요 시간
    tk = [int(input()) for _ in range(n)]

    tk.sort()
    L = 1
    R = tk[-1] * m      # 최대소요시간 * m
    times = [0] * n     # 심사대 별 심사횟수
    while L <= R:
        mid = (R + L) // 2
        for i in range(n):
            times[i] = mid // tk[i]       # 심사대 별 최대소요시간 기준 심사횟수
        sum_times = sum(times)          # 총 심사횟수
        if sum_times < m:
            L = mid + 1
        else:
            R = mid - 1
            ans = mid

    print(f'#{case}', ans)
