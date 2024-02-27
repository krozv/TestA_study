T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    res = 0
    for i in range(100):
        now = 0
        for j in range(100):
            # 1 밑에 2가 있으면 교착됨
            if arr[j][i] == 1:
                now = 1
            elif arr[j][i] == 2:
                if now == 1:
                    res += 1
                    now = 0
    print(f'#{tc} {res}')