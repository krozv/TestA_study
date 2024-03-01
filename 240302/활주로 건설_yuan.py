
# 높이가 같을때는 cnt+1
# 높이가 높아질때 cnt 가 x보다 작으면 return 0
# 높이 높아지고cnt 가 x보다 크면 cnt=1 로 돌아가기
# 높이가 낮아질때 cnt = -x+1 로 돌아가기
#### 높이가 두번 낮아지면 업데이트가 두번 되기때문에 이전 낮음이 반영이 안될 수있음
# 따라서 낮아졌을때 cnt 상태 한번 확인해주기

# 최종 cnt가 0보다 크면 최종 1
#외의 경우에는 return
x= 2
# lst 는 [3, 3, 3, 2, 2, 1]
# lst 는 [2, 2, 2, 3, 3, 1]
def f(lst):
    cnt = 1
    for x in range(1, len(lst)):
        # 같을때
        if lst[x-1] == lst[x]:
            cnt += 1

        # 높아질때
        elif lst[x-1] + 1 == lst[x]:
            if cnt >= A:
                cnt = 1  # 높아짐+ 이전 활주로 건설됐을때 cnt 초기화
            else:
                return False

        # 낮아질때
        elif lst[x - 1] - 1 == lst[x]:
            if cnt < 0:
                return False
            cnt = -A + 1

        else:
            return False  # 2차이면 return False

    if cnt >= 0:
        return True
    else:
        return False


T = int(input())
for tc in range(1,T+1):
    N, A = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    # 행검사
    res = 0
    for i in range(N):
        row = []  # 한줄 넣기
        for j in range(N):
            row.append(arr[i][j])
        if f(row):
            res +=1

    for i in range(N):
        col = []
        for j in range(N):
            col.append(arr[j][i])
        if f(col):
            res +=1


    print(f"#{tc} {res}")


