def rotate(num_list):
    return [num_list.pop()] + num_list

T = int(input())
for tc in range(1,T+1):

    N, K = map(int,input().split())
    # N은 4의 배수다(8이상28이하), 주어지는 암호 총 길이

    # 자물쇠의 비밀번호는 보물상자에 적힌 숫자로 만들 수 있는 모든 수 중 K번째로  큰 수를 10진수로 만든 수
    # - 적힌 숫자로 만들 수 있는 수들을 sort and reverse한 후 K번째를 찾자

    num_list = list(input())
    block = N//4 # 한 변의 암호 길이
    total_num = []
    for _ in range(block):
        for i in range(4):  # 4 개의 면
            total_num += [int(''.join(num_list[block*i:i*block + block]),16)]
            # 12면 123 456 789 101112
            # 16면 1234 5678 9101112 13141516
        num_list = rotate(num_list)
    
    total_num = sorted(list(set(total_num)), reverse = True)
    print(f"#{tc} {total_num[K-1]}")