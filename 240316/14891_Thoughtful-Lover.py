'''
14891. 톱니바퀴

총 8개의 톱니를 가진 톱니바퀴 4개
톱니는 N극 또는 S극
왼쪽부터 1~4번 톱니바퀴

톱니바퀴를 총 K번 회전
톱니바퀴의 회전은 한 칸을 기준
회전은 시계 방향 또는 반시계 방향

회전 방향에 따라 회전
회전하기 전 맞닿은 부분의 극이 다르면 옆에는 회전한 방향과 반대방향으로 회전

최종 상태를 구하는 프로그램

첫째줄부터 넷째줄까지 톱니바퀴의 상태
12시방향부터 시계방향 순서대로
N극은 0, S극은 1

다섯째줄 회전 횟수 K
다음 K개의 정수 묶음
첫 번째 정수는 회전시킬 톱니바퀴 번호, 두 번째 정수는 방향
1은 시계, -1은 반시계

1, 2, 3, 4 번 톱니바퀴의 12시 방향이 N극이면 0점,
S극이면 각각 1, 2, 4, 8 점
'''

# deque 를 이용할거야 !
from collections import deque


# 톱니바퀴를 회전하는 함수 rotate를 정의
def rotate(number, direction):
    # 이미 회전한 톱니바퀴라면 돌아가
    if rotate_check[number] == 1:
        return

    # 그게 아니면 우선 회전했다고 체크하고
    rotate_check[number] = 1

    # 시계 방향 회전
    if direction == 1:
        # 맨 뒤에 하나를 빼서 제일 앞으로 넣으면 됨
        gear[number].appendleft(gear[number].pop())

        # 오른쪽 톱니바퀴를 체크, 범위 안에 있고 서로 다른 극이면 회전해보자
        if number+1 <= 3 and adj[number][1] != adj[number+1][0]:
            rotate(number+1, -direction)
        # 왼쪽 톱니바퀴를 체크, 범위 안에 있고 서로 다른 극이면 회전해보자
        if number-1 >= 0 and adj[number][0] != adj[number-1][1]:
            rotate(number-1, -direction)

    # 반시계 방향 회전
    else:
        # 맨 앞에 하나를 빼서 제일 뒤로 넣으면 됨
        gear[number].append(gear[number].popleft())

        # 상동
        if number+1 <= 3 and adj[number][1] != adj[number+1][0]:
            rotate(number+1, -direction)
        if number-1 >= 0 and adj[number][0] != adj[number-1][1]:
            rotate(number-1, -direction)


# 12시에 위치한 톱니바퀴의 극을 확인해서 점수를 계산하는 함수 score 를 정의
def score():
    score = 0
    for i in range(4):
        if gear[i][0] == '1':
            score += 2 ** i
    return score


# 하나의 deque 안에 톱니바퀴 각각의 배열을 deque로
gear = deque(deque(input()) for _ in range(4))

K = int(input())
for _ in range(K):
    n, d = map(int, input().split())

    # 각각의 명령에 대해 회전하고 난후 인접 톱니바퀴의 회전여부를 판단해야하므로 미리 저장해둔다.
    adj = deque()
    for i in range(4):
        adj_sub = deque()
        adj_sub.append(gear[i][6])
        adj_sub.append(gear[i][2])
        adj.append(adj_sub)

    # 이미 회전한 톱니바퀴는 회전하지 말아야하므로
    rotate_check = [0] * 4

    # 입력은 톱니바퀴의 번호로 하지만, 톱니바퀴 배열은 인덱스로 되어 있으므로 하나 빼준다.
    rotate(n-1, d)

print(score())

'''
막 신나게 재귀로 해서 풀었는데 멈추지가 않더라
그래서 4번까지만 해보자 했는데 중복으로 되더라
그래서 check_list를 만들어봤지 뭐야
'''