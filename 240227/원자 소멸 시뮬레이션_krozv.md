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
                    
                    #없애줄 리스트를 작성후 한번에 제거?
                    
                    
    print(f'#{tc} {int(energy)}')
```
일단 시간좀 줄여야 할듯. 답은 맞게 나옴

### 2차 시도
8/50 시간초과.. + 테스트케이스 1번도 틀림
```python
di = [0.5,-0.5,0,0]
dj = [0,0,-0.5,0.5]

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)] #datum은 순서대로 x위치,y위치,이동방향,보유 에너지 k

    energy = 0
    for _ in range(4000): #4000번 반복 최대 위치차가 2000이고 0.5씩 움직인다면 4000번 움직여야 만날수나 있지..
        for datum in data:
            datum[0] += di[datum[2]]
            datum[1] += dj[datum[2]]

        for i in range(N-1):
            for j in range(i+1, N):
                if data[i][0] == data[j][0] and data[0][1] == data[j][1]:
                    energy += data[i][3] + data[j][3] #에너지 더해주기
                    data[i][3] = 0 #1번 원자의 에너지 없애주기(중복되서 더해지는 일이 없어야 하므로)
                    data[j][3] = 0 #2번 원자의 에너지 없애주기
    print(f'#{tc} {int(energy)}')
```

음.. remove하면서 시간을 줄여야 하나???
###3차 시도
9/50 테스트케이스 돌아가는 시간은 조금 줄은 듯
```python
di = [0.5, -0.5, 0, 0]
dj = [0, 0, -0.5, 0.5]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]  # datum은 순서대로 x위치,y위치,이동방향,보유 에너지 k

    energy = 0

    remove_index = []
    for _ in range(4000):  # 대에충 4000번 반복 최대 위치차가 2000이고 0.5씩 움직인다면 4000번 움직여야 만날수나 있지..
        for datum in data:
            datum[0] += di[datum[2]]
            datum[1] += dj[datum[2]]

        for datum1 in data:
            for j,datum2 in enumerate(data):
                if datum1[0] == datum2[0] and datum1[1] == datum2[1] and datum1 != datum2:
                    energy += datum1[3] + datum2[3]  # 에너지 더해주기
                    datum1[3] = 0  # 1번 원자의 에너지 없애주기
                    datum2[3] = 0
                    # 없애줄 인덱스 리스트를 작성후 한번에 제거?
                    remove_index.append(j)

        while remove_index:
            remove_index.sort()
            idx = remove_index.pop()
            data.pop(idx)
    print(f'#{tc} {energy}')
```

### 4차 시도
9/50 시간초과
```python
di = [0.5, -0.5, 0, 0]
dj = [0, 0, -0.5, 0.5]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]  # datum은 순서대로 x위치,y위치,이동방향,보유 에너지 k

    energy = 0

    remove_index = []
    for _ in range(4000):  # 대에충 4000번 반복 최대 위치차가 2000이고 0.5씩 움직인다면 4000번 움직여야 만날수나 있지..
        for datum in data:
            datum[0] += di[datum[2]]
            datum[1] += dj[datum[2]]
        for datum1 in data:
            for j,datum2 in enumerate(data):
                if datum1[0] == datum2[0] and datum1[1] == datum2[1] and datum1 != datum2 and (datum1[3] != 0 or datum2[3] != 0):
                    energy += datum1[3] + datum2[3]  # 에너지 더해주기
                    datum1[3] = 0  # 1번 원자의 에너지 없애주기
                    datum2[3] = 0
                    # 없애줄 인덱스 리스트를 작성후 한번에 제거?
                    remove_index.append(j)
                elif datum2[0] > 1000 or datum2[0] <-1000 or datum2[1]>1000 or datum2[1]<-1000:
                    remove_index.append(j)

        while remove_index:
            print(remove_index)
            remove_index = list(set(remove_index))
            remove_index.sort()
            idx = remove_index.pop()
            data.pop(idx)
    print(f'#{tc} {energy}')
```

### 5차
딕셔너리로 같은 위치에 있는 애들 넣어서 처리할라 했는데...

9/50 fail
```python
di = [0.5, -0.5, 0, 0]
dj = [0, 0, -0.5, 0.5]
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]  # datum은 순서대로 x위치,y위치,이동방향,보유 에너지 k
    energy = 0
    remove_index = []
    repeat = 0
    while repeat < 4000 and len(data)>1:  # 대에충 4000번 반복 최대 위치차가 2000이고 0.5씩 움직인다면 4000번 움직여야 만날수나 있지..
        repeat += 1
        for datum in data:
            datum[0] += di[datum[2]]
            datum[1] += dj[datum[2]]
        location = {}
        for datum in data: #location에 같은 위치를키로, 같은 위치 녀석들을 묶어서 벨류 값으로 이용
            try:
                location[(datum[0], datum[1])].append(datum)
            except:
                location[(datum[0],datum[1])] = [datum]

        data = []
        for l in location:
            if len(location[l]) >= 2: #벨류가 2이상, 즉 같은 위치에 여러 원자가 있다면
                for atom in location[l]:
                    energy += atom[3]
            else:#정상범위내에 있고, 현재 위치에 원자가 1개만 있다면 다시 data에 넣어준다.
                if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000:
                    data.append(location[l][0])

    print(f'#{tc} {energy}')

```

### 아오... 복붙 코드
pass
```python
T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    atom = [list(map(int, input().split())) for _ in range(n)]
    # 격자 중간에서 만날 수도 있기 때문에 0.5초 단위로 이동한다고 가정했음
    d = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

    result = 0

    # 아톰 개수가 2개 이하가 되면 만날 아톰이 없으니까 종료
    while len(atom) >= 2:
        # 모든 아톰을 0.5초 단위로 이동시킨다
        for i in range(len(atom)):
            atom[i][0] = atom[i][0] + d[atom[i][2]][0]
            atom[i][1] = atom[i][1] + d[atom[i][2]][1]

        # 좌표를 딕셔너리로 표현
        location = {}
        # 각 아톰들을 순회하면서 좌표: [아톰들]의 형태로 넣어준다.
        for a in atom:
            try:
                location[(a[0], a[1])].append(a)
            except Exception:
                location[(a[0], a[1])] = [a]

        # 아톰 리스트를 초기화하고
        atom = []
        for l in location:

            if len(location[l]) >= 2:
                # 만약 같은 위치에 아톰이 여러개라면 결과값에 아톰의 에너지들을 결과값에 넣어주고
                for at in location[l]:
                    result += at[3]
            else:
                # 위치에 아톰이 1개라면 범위내에 있는 아톰들은 아톰 리스트에 다시 넣어준다.
                if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000:
                    atom.append(location[l][0])

    print(f'#{tc}', result)
```