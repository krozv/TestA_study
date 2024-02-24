T = int(input())
for tc in range(1, T + 1):
    N = input()  # 문자열로 받기
    k = 1
    digit_lst = []

    while len(digit_lst) != 10:
        x = int(N) * k
        lst = list(str(x))  # lst = ['1','2','3', ...]
        for i in lst:
            if i not in digit_lst:
                digit_lst.append(i)

        k += 1
    print(f'#{tc} {x}')