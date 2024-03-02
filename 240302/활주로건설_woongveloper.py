'''
matrix 숫자 : 높이 의미, 행별로 열별로 활주로 건설 가능 여부 체크
높이가 다른 경우 활주로 건설하려면 경사로 요구
경사로는 가로 x, 세로 1이며 이를 활용해 연결했을 때, 경사를 이을 수 있다면 건설 가능
'''
'''
주어진 matrix를 분석하는 (행과 열 각각) 함수를 정의한다.
함수를 구성할 땐, 숫자를 하나하나 보고, 이전과 다른 숫자가 있다면
그 숫자가 이전의 숫자와 1 차이가 난다면 경사로 설치를 시작한다.
경사로가 x번 설치되기 전, 또 다른 수를 만난다면 경사로 설치가 불가능 하다는 것을 의미한다.
'''
def check_i(i):
    # i행의 활주로 건설 여부 판단 함수
    prev = matrix[i][0]
    result = []
    memory = []
    for j in range(N):
        if prev == matrix[i][j]:
            memory += [matrix[i][j]]
        elif abs(prev-matrix[i][j]) == 1:
            #단차가 1인 경우
            result += [[memory[0], len(memory)]]
            memory = [matrix[i][j]]
            prev = matrix[i][j]
        elif abs(prev-matrix[i][j]) >= 2:
            return False
    result += [[memory[0], len(memory)]]
    
    need_slide = len(result) - 1
    # 필요한 슬라이드 갯수
    for k in range(need_slide):
        # 두 단차를 비교한다. 좌측이 큰지 우측이 큰지, 낮은 쪽에 슬라이드 설치 여부를 판단한다.
        if result[k][0] > result[k+1][0]: #좌측이 더 크다면, 우측에 설치해야한다.
            result[k+1][1] = result[k+1][1] - x #우측에 슬라이드 공간이 확보된다면
            if result[k+1][1] >= 0:
                continue
            else:
                return False # 공간이 확보되지 않는다면
        elif result[k][0] < result[k+1][0]: # 우측이 더 크다면 좌측에 설치해야한다.
            result[k][1] = result[k][1] - x
            if result[k][1] >= 0: # 좌측에 슬라이드 공간이 확보된다면
                continue
            else:
                return False
    else:
        return True

def check_j(j):
    # j열의 활주로 건설 여부 판단 함수
    prev = matrix[0][j]
    result = []
    memory = []
    for i in range(N):
        if prev == matrix[i][j]:
            memory += [matrix[i][j]]
        elif abs(prev-matrix[i][j]) == 1:
            #단차가 1인 경우
            result += [[memory[0], len(memory)]]
            memory = [matrix[i][j]]
            prev = matrix[i][j]
        elif abs(prev-matrix[i][j]) >= 2:
            return False
    result += [[memory[0], len(memory)]]
    
    need_slide = len(result) - 1
    # 필요한 슬라이드 갯수
    for k in range(need_slide):
        # 두 단차를 비교한다. 좌측이 큰지 우측이 큰지, 낮은 쪽에 슬라이드 설치 여부를 판단한다.
        if result[k][0] > result[k+1][0]: #좌측이 더 크다면, 우측에 설치해야한다.
            result[k+1][1] = result[k+1][1] - x #우측에 슬라이드 공간이 확보된다면
            if result[k+1][1] >= 0:
                continue
            else:
                return False # 공간이 확보되지 않는다면
        elif result[k][0] < result[k+1][0]: # 우측이 더 크다면 좌측에 설치해야한다.
            result[k][1] = result[k][1] - x
            if result[k][1] >= 0: # 좌측에 슬라이드 공간이 확보된다면
                continue
            else:
                return False
    else:
        return True

T = int(input())
for tc in range(1,T+1):
    N, x = map(int,input().split())
    matrix = []
    for _ in range(N):
        matrix += [list(map(int,input().split()))]
    cnt = 0
    for k in range(N):
        if check_i(k) == True:
            cnt += 1
        if check_j(k) == True:
            cnt += 1
    print(f"#{tc} {cnt}")