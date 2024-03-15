# 17822. 원판돌리기
### 코드
pypy3-336ms
```python
from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int,input().split()) #N:최대원판크기, M: 원판에 적힌 수
data = deque()
for _ in range(N):
    data.append(deque(map(int,input().split()))) #데크를 데이터에 넣어주기

# print('초기 data')
# for datum in data:
#     print(datum)
for t in range(T):
    x, d, k = map(int, input().split()) #x:원판크기, d: 0-시계, 1-반시계, k 회전시킬 횟수
    for i in range(N):
        if (i+1) % x == 0: #i번 원판(원판의 크기는 i+1)크기가 x의 배수인 경우
            if d == 0:  # 시계방향
                data[i].rotate(k)
            else:
                data[i].rotate(-k)

    # print(f'{t+1}번째 회전 후')
    # for datum in data:
    #     print(datum)

    #인접확인
    remove_set = set()
    for i in range(N):
        for j in range(M):
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if (i == 0 and ni == -1) or (i == N-1 and ni == N):
                    continue
                ni = (ni)%N if ni>=0 else N-1
                nj = (nj)%M if nj>=0 else M-1
                if data[i][j] == data[ni][nj] and data[i][j] != 'x':
                    remove_set.add((i,j))
                    remove_set.add((ni,nj))

    if len(remove_set): #지울게 있는 경우
        for r,c in remove_set:
            data[r][c] = 'x'
        # print(f'{t+1}번째 제거 후')
        # for datum in data:
        #     print(datum)
    else:       #지울 녀석들이 없는 경우
        cnt = 0         #0이 아닌 숫자들
        nums_sum = 0
        for i in range(N):
            for j in range(M):
                if data[i][j] != 'x':
                    cnt += 1
                    nums_sum += data[i][j]
        if cnt != 0:
            everage = nums_sum/cnt
            # print(f'{t+1}번째 평균값 : {everage}')
            for i in range(N):
                for j in range(M):
                    val = data[i][j]
                    if val != 'x':
                        if val < everage:
                            data[i][j] += 1
                        elif val > everage:
                            data[i][j] -= 1################################# 여기가 제대로 작동을 안하네
                    
            # print(f'{t+1}번째 인접한게 없어서 다른 평균값과 비교해서 바꾼후 data')
            # for datum in data:
            #     print(datum)
result = 0
for i in range(N):
    for j in range(M):
        if data[i][j] != 'x':
            result += data[i][j]
# print('최종 모양')
# for datum in data:
#     print(datum)
print(result)
```