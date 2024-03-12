# 14891. 톱니바퀴
```python
from collections import deque

gears = [deque(input()) for _ in range(4)]
K = int(input()) #회전횟수
rotate = [list(map(int,input().split())) for _ in range(K)]

for i in range(K): #K번의 회전
    r_gear = rotate[i][0] - 1  #회전시킬 기어 인덱스
    d = rotate[i][1]    

    gear_rotate = [0,0,0,0]
    gear_rotate[r_gear] = d
    #왼쪽 기어들 계속 확인
    while r_gear > 0: 
        if gears[r_gear-1][2] != gears[r_gear][-2]:
            gear_rotate[r_gear-1] = -gear_rotate[r_gear]
            r_gear -= 1
        else:
            break
    r_gear = rotate[i][0] - 1  #회전시킬 기어 인덱스
    d = rotate[i][1] 

    #오른쪽 기어들 계속 확인
    while r_gear < 3:
        if gears[r_gear][2] != gears[r_gear+1][-2]:
            gear_rotate[r_gear+1] = -gear_rotate[r_gear]
            r_gear += 1
           
        else:
            break

    for i, r in enumerate(gear_rotate):
        if r == 1:      #시계
            gears[i].appendleft(gears[i].pop())
        elif r == -1:   #반시계
            gears[i].append(gears[i].popleft())
    
result = 0
for i in range(4):
    if gears[i][0] == '1': # S극
        result += 2**i

print(result)
```