T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = list(str(N))
    i = 1
    while True:
        num_list += (list(str(N * i)))
        if len(set(num_list)) == 10:
            break
        i += 1
    print(f'#{tc}',N * i)
