

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    lst = list(input())
    num = N//4

    set_res = set()
    for i in range(N):
        x=''
        for j in range(num):
            x+= lst[(i+j)%N]
        if x not in set_res:
            set_res.add(x)
    set_res = sorted(set_res, reverse= True)

    print(f'#{tc} {int(list(set_res)[K-1],16)}')
