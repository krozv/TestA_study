def f2(check):
    global min_v
    # 5가 아닌 범위 색칠하기
    total = [0] * 5
    for r in range(N+1):
        for c in range(N+1):
            if check[r][c]:
                total[4] += arr[r][c]
            # 1범위
            elif 1 <= r < x+d1 and 1 <= c <= y:
                total[0] += arr[r][c]
            # 2범위
            elif 1 <= r <= x+d2 and y < c <= N:
                total[1] += arr[r][c]
            # 3범위
            elif x+d1 <= r <= N and 1 <= c < y-d1+d2:
                total[2] += arr[r][c]
            # 4범위
            elif x+d2 < r <= N and y-d1+d2 <= c <= N:
                total[3] += arr[r][c]

    min_v = min(min_v, max(total) - min(total))
    return


def f(x,y,d1,d2):
    # 경계선 칠하기
    check = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(d1+1):
        check[x+i][y-i] = 1
    for i in range(d2+1):
        check[x+i][y+i] = 1
    for i in range(d2+1):
        check[x+d1+i][y-d1+i] = 1
    for i in range(d1+1):
        check[x+d2+i][y+d2-i] = 1

    # 경계선 내부 채우기
    for j in range(N+1):
        lst = []
        flag = 0
        for i in range(N+1):
            if check[i][j]:
                flag = 1
            if flag:
                lst.append((i,j))

            if check[i][j] and flag:
                for (x,y) in lst:
                    check[x][y] = 1

    f2(check)

N = int(input())
arr = [[0]*(N+1)] + [ [0] + list(map(int, input().split()))for _ in range(N)]

min_v = 100* 20*20
# print(arr)
for x in range(1,N+1):
    for y in range(1,N+1):
        # 대각선 깅이 최대 N-1, 그때의 d는 N-2
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                # x,y,d1,d2 조건넣기
                    f(x,y,d1,d2)

print(min_v)

