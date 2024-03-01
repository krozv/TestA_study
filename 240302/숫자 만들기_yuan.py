

def dfs(i,s): #s 는 직전까지의 계산 값
    global mins
    global maxs
    global c1,c2,c3,c4

    if i == N: # 1부터 시작해서 연산자 횟수만큼 돌기
        if s > maxs:
            maxs = s
        if s < mins:
            mins = s
        return

    else:
        #+
        if c1 >0 :
            s += d_lst[i]
            c1 -=1
            dfs(i+1,s)
            s -= d_lst[i]
            c1+=1


        #-
        if c2 >0 :
            s -= d_lst[i]
            c2-=1
            dfs(i+1,s)
            s += d_lst[i]
            c2+=1


        #*
        if c3 >0 :
            s *= d_lst[i]
            c3-=1
            dfs(i+1,s)
            s = int(s/d_lst[i])
            c3+=1

        # /
        if c4 > 0:
            s = int(s / d_lst[i])
            c4 -= 1
            dfs(i + 1, s)
            s *= d_lst[i]
            c4 += 1



T = int(input())
for tc in range(1,T+1):
    N= int(input()) # 카드 N개 연산자 카드 N-1개

    # +, -, * /
    c_lst = list(map(int,input().split()))
    c1,c2,c3,c4 = c_lst[0],c_lst[1],c_lst[2],c_lst[3]

    d_lst = list(map(int,input().split()))

    mins = 100000000
    maxs = -100000000

    dfs(1,d_lst[0])
# print(maxs,mins)
    print(f'#{tc} {maxs-mins}')
