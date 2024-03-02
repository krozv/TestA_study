# 3074. 입국심사
### 결국은 구글을 통해 찾은 성공 코드
1207ms. 이분 탐색 사용
```python
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) #N은 심사대 수, M은 사람수
    times = [int(input()) for _ in range(N)]
    left = 1
    right = max(times) * M#최악의 시간을 right로 둠

    while left <= right:
        mid = (left + right)//2 #중간값

        people = 0
        for time in times:
            people += mid//time #각 심사대에서 수용할 수 있는 인원을 더해줌
            if people >= M: #mid라는 시간동안 M명이상 수용가능한격우
                break

        if people >= M:#mid라는 시간동안 M명이상 수용가능한 경우
            min_time = mid
            #시간을 줄여야 하니 right를 줄임
            right = mid - 1
        else:
            left = mid + 1
    print(f'#{tc} {min_time}')
```


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
### 최소공배수 이용 코드
최소공배수 이용해서 풀라했으나 내가 푼 방법은 3.9이상 버전에서만 가능한듯..
```python
from math import lcm

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) #N은 심사대 수, M은 사람수
    data = [[0,0] for _ in range(N)] # [i번째 테이블에서 총 걸릴 시간, 그 테이블의 한 사람당 처리 시간]

    num = 1 #최소 공배수를 찾기 위한 숫자
    for i in range(N):
        data[i][1] = int(input())
        num = lcm(data[i][1],num) ##이녀석 python3.9부터 사용가능하다는데 swea는 3.7ver임...
    #여기 나올 num은 동시에 심사가 끝날 시간(최소공배수)
    cycle = 0 #한 사이클당 처리가능한 사람 수
    for datum in data:
        cycle += num // datum[1]
    repeat = M//cycle #cycle돌릴 수 있는 횟수
    M = M % cycle #repeat만큼 사이클을 돌리고 남은 사람 수
    for _ in range(M):
        data.sort(key= lambda x: x[0]+x[1])
        data[0][0] += data[0][1]
    data.sort(key=lambda x: x[0])
    print(f'#{tc} {num*repeat + data[N-1][0]}')
```

### 또 다른 방법으로 최소공배수 이용
3/10 시간초과.. 이 방법도 아닌듯...
```python
from math import gcd

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) #N은 심사대 수, M은 사람수
    data = [[0,0] for _ in range(N)] # [i번째 테이블에서 총 걸릴 시간, 그 테이블의 한 사람당 처리 시간]
    num = 1 #최소 공배수를 찾기 위한 숫자
    for i in range(N):
        data[i][1] = int(input())
        num = (data[i][1]*num)//gcd(data[i][1],num) 
    #여기 나올 num은 동시에 심사가 끝날 시간(최소공배수)
    cycle = 0 #한 사이클당 처리가능한 사람 수
    for datum in data:
        cycle += num // datum[1]
    repeat = M//cycle #cycle돌릴 수 있는 횟수
    M = M % cycle #repeat만큼 사이클을 돌리고 남은 사람 수
    for _ in range(M):
        data.sort(key= lambda x: x[0]+x[1])
        data[0][0] += data[0][1]
    data.sort(key=lambda x: x[0])
    print(f'#{tc} {num*repeat + data[N-1][0]}')
```