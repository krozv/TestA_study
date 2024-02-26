# 5648. 원자 소멸 시뮬레이션 
### 첫 시도
9/50 시간초과...
```python
# 뭔가 0.5단위로 끊어서 움직여야 할듯
#방향 상(0), 하(-1),좌(2),우(3)
di = [0.5,-0.5,0,0]
dj = [0,0,-0.5,0.5]

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)] #datum은 순서대로 x위치,y위치,이동방향,보유 에너지 k

    energy = 0
    for _ in range(4000): #대에충 4000번 반복 최대 위치차가 2000이고 0.5씩 움직인다면 4000번 움직여야 만날수나 있지..
        for datum in data:
            datum[0] += di[datum[2]]
            datum[1] += dj[datum[2]]

        for datum1 in data:
            for datum2 in data:
                if datum1[0] == datum2[0] and datum1[1] == datum2[1] and datum1 != datum2:
                    energy += datum1[3] + datum2[3] #에너지 더해주기
                    datum1[3] = 0 #1번 원자의 에너지 없애주기
                    datum2[3] = 0 #2번 원자의 에너지 없애주기
    print(f'#{tc} {int(energy)}')
```

일단 시간좀 줄여야 할듯. 답은 맞게 나옴