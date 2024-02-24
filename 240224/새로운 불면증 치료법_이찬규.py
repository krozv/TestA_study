# 양을 세는 함수 counting_shhep 을 정의
def counting_sheep(n):
    global cnt
    # num_check 에 0이 없을 때까지
    while 0 in num_check:
        # n 의 배수를 돌아가며
        cnt += 1
        sheep = N * cnt
        # 수를 체크
        while sheep != 0:
            num_check[sheep%10] = 1
            sheep //= 10


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 0~9 까지 수 중 봤던 수들을 체크하는 리스트 num_check
    num_check = [0] * 10
    # 셀 양의 배수를 만들어 줄 cnt
    cnt = 0

    counting_sheep(N)

    print(f'#{tc} {N*cnt}')