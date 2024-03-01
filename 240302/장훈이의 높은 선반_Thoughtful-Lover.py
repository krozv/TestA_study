'''
1486 .
장훈이의 높은 선반

점원들의 키를 합친 탑의 높이가 선반보다 이상인 탑 중에서 가장 낮은 탑을 알아내려고 한다.

T : 테스트 케이스 수
N, B : 직원의 수 N, 선반의 높이 B
직원들 키의 배열

부분집합
'''

'''
1
5 16
1 3 3 5 6

내가 만든 테케
1
8 12
1 2 2 3 4 5 8 9
'''


'''# 뭔가 잘 안될 것 같았음
# 재귀로 해야지
def human_tower(idx, target):
    global height_sum

    # 종료 조건
    if target < M:
        return

    # 만약 키가 M값보다 크면 우선 다음 점원을 탐색
    if arr[n] > M:
        human_tower(idx-1, target)

    # 만약 앞에 킼킼
    if n ! -1 and height_sum == 0:
        height_sum += arr[n+1]
        return
    height_sum += arr[n]
    if height_sum >= B:
        return height_sum-M


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    height_sum = 0

    human_tower(-1, B)

    print(f'#{tc} {human_sum-M}')'''


# 인덱스를 순회하며 점원들의 키를 더해갈 함수 human_tower 를 정의. 매개변수는 n 번째 점원의 키를 더할 차례, s 는 현재까지의 키를 더한 값
def human_tower(n, s):
    global height_sum

    # 앞에 선택한 값 이후에 있는 값들 중에 하나를 선택하고
    for i in range(n+1, N):
        # 합에 더해주고
        s += arr[i]
        # 이 합이 B보다 큰 값 중 현재까지 최소값이라면, height_sum 을 갱신해주고
        if B <= s < height_sum:
            height_sum = s
        # 만약 마지막 마지막 직원을 더하고 있다면, 함수를 종료
        if i == N-1:
            return
        # 다음 값으로 넘어감
        human_tower(i, s)
        # 재귀를 마치면 다시 값을 빼주고 다음 시행으로 넘어감
        s -= arr[i]


T = int(input())
# 각 테스트 케이스별 시행
for tc in range(1, T+1):
    # 점원의 수 N, 선반의 높이 B
    N, B = map(int, input().split())
    # 점원들의 키가 담긴 리스트
    arr = list(map(int, input().split()))
    # M 이상인 점원들의 키의 합 중 가장 작은 값을 저장할 height_sum. 초기값은 점원들 키를 모두 더한 값의 최대값
    height_sum = 10000 * N

    # 인간 탑을 쌓아보자!
    human_tower(-1, 0)

    print(f'#{tc} {height_sum-B}')
