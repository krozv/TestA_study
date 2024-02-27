# Magnetic
"""
반복문 동일하게 이용
"""
T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        test = True
        while test:
            for i in range(N):
                if arr[i][j] == 1:
                    # 탈출
                    if i+1 > N-1:
                        arr[i][j] = 0
                    else:
                        # 이동 가능
                        if arr[i+1][j] == 0:
                            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                        # 이동 불가능
                        else:
                            if arr[i+1][j] == 4:
                                arr[i][j] = 4
                            elif arr[i+1][j] == 2:
                                arr[i][j] = 4
                                cnt += 1
                # S극
                elif arr[i][j] == 2:
                    # 탈출
                    if i-1 < 0:
                        arr[i][j] = 0
                    else:
                        # 이동 가능
                        if arr[i-1][j] == 0:
                            arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
                        # 이동 불가능
                        else:
                            if arr[i-1][j] == 4:
                                arr[i][j] = 4
                            else:
                                arr[i][j] = 4
            test = True
            for i in range(N):
                if arr[i][j] != 1 and arr[i][j] != 2:
                    test = False
    print(f'#{t} {cnt}')