# 4014. 활주로 건설
### 코드
181ms 코드 좀 더러움...
```python
T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())  # N:한변크기, X:경사로의 길이
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 활주로 건설 가능 경우의 수

    for i in range(N): #행방향으로 먼저 탐색
        pre_height = data[i][0]
        up_cnt = 0  # 갑자기 높이가 커질때 경사로를 놓을 수 있을지 확인하기 위함
        down_cnt = 0  # 갑자기 높이가 낮아질때 경사로 사용할 수 있는지 확인하기 위함
        down_possible = True
        possible = True
        for j in range(N):
            if down_possible == False and down_cnt >= X:
                down_possible = True
                up_cnt = 0
            if data[i][j] == pre_height:  # 연속해서 같은 숫자일때
                up_cnt += 1
                down_cnt += 1
            elif data[i][j] == pre_height + 1:  # 현 위치가 전 위치보다 1높아지면
                if up_cnt >= X:  # 업 cnt가 경사로 길이 이상이면
                    up_cnt = 1  # 다시 초기화
                    pre_height += 1
                else:  # 경사로 못놓는다면
                    possible = False
                    break  # 다음 반복으로 넘어가라~
            elif data[i][j] == pre_height - 1:  # 현 위치가 전 위치보다 1낮아지면
                if down_possible:
                    pre_height -= 1
                    down_possible = False
                    down_cnt = 1
                    up_cnt = 0  # 당장 내려가는 경사로부터 생각해야하니 0으로 바뀜
                else:  # 경사로 놔야하는데 못놓은상태에서 또 놔야한다네...
                    possible = False
                    break
            else:  # 무언가 그전거랑 같지 않거나 gap이 1을 초과할 경우
                possible = False
                break
        if possible:
            if down_cnt >= X:
                down_possible = True
            if down_possible:
                result += 1
    
    #그냥 똑같은걸 열방향으로 진행 한 것
    for j in range(N):
        pre_height = data[0][j]
        up_cnt = 0  # 갑자기 높이가 커질때 경사로를 놓을 수 있을지 확인하기 위함
        down_cnt = 0  # 갑자기 높이가 낮아질때 경사로 사용할 수 있는지 확인하기 위함
        down_possible = True
        possible = True
        for i in range(N):
            if down_possible == False and down_cnt >= X:
                down_possible = True
                up_cnt = 0
            if data[i][j] == pre_height:  # 연속해서 같은 숫자일때
                up_cnt += 1
                down_cnt += 1
            elif data[i][j] == pre_height + 1:  # 현 위치가 전 위치보다 1높아지면
                if up_cnt >= X:  # 업 cnt가 경사로 길이 이상이면
                    up_cnt = 1  # 다시 초기화
                    pre_height += 1
                else:  # 경사로 못놓는다면
                    possible = False
                    break  # 다음 반복으로 넘어가라~
            elif data[i][j] == pre_height - 1:  # 현 위치가 전 위치보다 1낮아지면
                if down_possible:
                    pre_height -= 1
                    down_possible = False
                    down_cnt = 1
                    up_cnt = 0  # 당장 내려가는 경사로부터 생각해야하니 0으로 바뀜
                else:  # 경사로 놔야하는데 못놓은상태에서 또 놔야한다네...
                    possible = False
                    break
            else:  # 무언가 그 전거랑 같지 않거나 gap이 1을 초과할 경우
                possible = False
                break
        if possible:
            if down_cnt >= X:
                down_possible = True
            if down_possible:
                result += 1
    print(f'#{tc} {result}')
```