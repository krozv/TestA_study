# 3074. 입국심사
### 첫 시도..
2/10 시간초과....
```python
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) #N은 심사대 수, M은 사람수
    times = [int(input()) for _ in range(N)]
    test_tables = [0]*N
    for _ in range(M): #사람 수 만큼 반복
        #다음에 넣었을 때 가장 시간이 적게 걸릴곳에 사람을 넣자
        min_pos = 0
        min_time = 1000000
        for j, test_table in enumerate(test_tables):
            if min_time > test_table+times[j]:
                min_time = test_table+times[j]
                min_pos = j  #다음에 사람 넣었을 때 가장 시간이 적게 걸릴 위치
        test_tables[min_pos] += times[min_pos]
    print(f'#{tc} {max(test_tables)}') #가장 많이 걸릴 곳의 시간 출력
```
### 두번째 시도
3/10 시간초과

sort사용
```python
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) #N은 심사대 수, M은 사람수
    data = [[0,0] for _ in range(N)] # [걸릴 시간, 그 테이블의 처리 시간]
    for i in range(N):
        data[i][1] = int(input())

    for _ in range(M):
        data.sort(key= lambda x: x[0]+x[1])
        data[0][0] += data[0][1]
    data.sort(key=lambda x: x[0])
    print(f'#{tc} {data[N-1][0]}')
```