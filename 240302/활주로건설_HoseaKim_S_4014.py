# 활주로 건설 swea 4014
T = int(input())
for case in range(1, T+1):
    # 한 변의 길이 (6 <= N <= 20), 경사로의 길이 (2 <= X <= 4)
    N, X = map(int, input().split())
    # 지형 높이 (1~6)
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):

        last = -1
        pre = 0
        for j in range(N):
            cnt = 0     # 경사로 놓을 칸수 셀 곳
            if pre:
                # 높이 차이가 2 이상일 때 -> 활주로 불가능
                if abs(pre - arr[i][j]) >= 2:
                    break
                # 한 칸 내려갈 때
                elif pre - arr[i][j] == 1:
                    # 경사로 놓기
                    for k in range(X):
                        if j+k < N and arr[i][j] == arr[i][j+k]:
                            cnt += 1
                    if cnt != X:
                        break
                    last = j+k
                # 한 칸 올라갈 때
                elif pre - arr[i][j] == -1:
                    # 경사로 놓기
                    for k in range(X):
                        if j-1-k > last and arr[i][j-1] == arr[i][j-1-k]:
                            cnt += 1
                    if cnt != X:
                        break
                    last = j-1
            pre = arr[i][j]
        else:
            # print('가로', i)
            ans += 1

        last = -1
        pre = 0
        for j in range(N):
            cnt = 0
            if pre:
                if abs(pre - arr[j][i]) >= 2:
                    break
                elif pre - arr[j][i] == 1:
                    for k in range(X):
                        if j + k < N and arr[j][i] == arr[j+k][i]:
                            cnt += 1
                    if cnt != X:
                        break
                    last = j+k
                elif pre - arr[j][i] == -1:
                    for k in range(X):
                        if j - 1 - k > last and arr[j-1][i] == arr[j-1-k][i]:
                            cnt += 1
                    if cnt != X:
                        break
                    last = j-1
            pre = arr[j][i]
        else:
            # print('세로', i)
            ans += 1

    print(f'#{case}', ans)
