'''
5658 .
[모의 SW 역량테스트] 보물상자 비밀번호

각 변에 16진수 숫자(0~F)가 적혀 있는 보물 상자
보물 상자 뚜겅을 시계방향으로 한 번 돌릴 때마다 한 칸씩 회전

각 변에 동일한 개수의 숫자 시계방향 순으로 높은 자리 숫자
자물쇠 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 숫자 중 K번째로 큰 수를 10진수로 만든 것
N개의 숫자가 주어질 때 보물상자의 비밀번호를 출력하는 프로그램

N은 4의 배수이고, 8이상 28이하의 정수이다. (8 ≤ N ≤ 28)
N개의 숫자는 각각 0이상 F이하로 주어진다. (A~F는 알파벳 대문자로만 주어진다.)
K는 생성 가능한 수의 개수보다 크게 주어지지 않는다.
'''

from collections import deque


# 비밀번호의 후보군이 되는 수들을 뽑아내주는 함수 lets_find_pw 를 정의
# 매개변수로 box_list 는 변화하는 box의 배열을, cnt = 회전 횟수를 받을 것임
def lets_find_pw(box_list, cnt):
    # 각 변에 적힌 16진수를 numbers 에 배정
    # 각 변의 자리수를 고정하고 여기에 변에 있는 수만큼 더해서 시행
    for i in range(4):
        num = ''
        for j in range(N//4):
            num += box_list[N//4*i+j]
        numbers.append(num)

    # 4변에 있는 모든 수를 뱆정하고 나면 cnt를 1 추가
    # 이때 변에 적힌 수만큼 회전하면 0회전과 동일해지기 때문에 함수를 종료
    cnt += 1
    if cnt == N//4:
        return

    # box_list의 제일 뒷수를 빼서 제일 처음으로 넣어줌
    pop_num = box_list.pop()
    box_list.appendleft(pop_num)

    lets_find_pw(box_list, cnt)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 박스에 적힌 수의 배열을 string deque 로 받아주고
    box = deque(input())
    # 여기서 뽑아 낸 수를 저장해줄 deque numbers 를 정의
    numbers = deque()

    # 함수를 호출
    lets_find_pw(box, 0)

    # 구한수를 집합으로 해서 중복을 없애주고, 다시 리스트로 바꿔줌
    numbers = set(numbers)
    numbers = list(numbers)

    # numbers의 전체 길이 L
    L = len(numbers)
    # numbers 전체를 순회하며 16진수를 2진수로 바꿔줄 예정정
    for k in range(L):
        numbers[k] = int(numbers[k], 16)
    # 내림차순으로 숫자를 정리
    numbers.sort(reverse=True)

    print(f'#{tc} {numbers[K-1]}')