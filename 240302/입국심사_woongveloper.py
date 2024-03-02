T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    tk_list = [int(input()) for _ in  range(n)]
    start, end = 1, m*(10**9) # 10**9 만으로 구성된 심사대
    while start <= end: # start, end가 역전되는 경우를 정지조건으로
        point = (start + end)//2
        total = sum([point // i for i in tk_list])
        if total < m:
            start = point + 1
        else:
            end = point - 1
            res = point
    print(f"#{tc} {res}")