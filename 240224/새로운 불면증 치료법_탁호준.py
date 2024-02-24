T = int(input())
for tc in range(1,1+T):
    N = int(input())
    nums = [0]*10 #숫자 i를 본 경우 nums[i] = 1 이 될 예정.
    now_lamb = 0 #현재 양 번호
    while sum(nums) != 10:#nums 값이 모두 1이 될때까지 반복
        now_lamb += N
        now_lamb_str = str(now_lamb)
        for i in now_lamb_str:
            nums[int(i)] = 1
    print(f'#{tc} {now_lamb}')