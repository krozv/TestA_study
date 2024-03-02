'''
N개의 숫자가 입력으로 주어졌을 때 K번째 숫자를 출력해라
'''
# 회전횟수구하는 계산식

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num_16_input = list(input())
    turn_num = N // 4
    rs = []
    for _ in range(turn_num):
        for i in range(4):
            start_idx = i * N//4
            end_idx = start_idx + N//4
            rs.append(''.join(num_16_input[start_idx:end_idx]))
        num_16_input = num_16_input[1:]+num_16_input[:1]
    result = list(set(rs))
    int_result = []
    for r in result:
        int_result.append(int(r,16))
    int_result.sort(reverse=True)

    print(f'#{tc} {int_result[K - 1]}')
