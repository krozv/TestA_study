# 보물상자 비밀번호 swea 5658
T = int(input())
for case in range(1, T+1):
    # 수의 개수 n, k번째 큰 수
    n, k = map(int, input().split())
    hexa = input()

    hex_set = set()
    for i in range(n//4):
        temp = [[0] * (n//4) for _ in range(4)]
        for x in range(n//4):
            temp[0][x] = hexa[x - i]
            temp[1][x] = hexa[x+n//4 - i]
            temp[2][x] = hexa[x+(n//4)*2 - i]
            temp[3][x] = hexa[x+(n//4)*3 - i]
        hex_set.update(set(map(tuple, temp)))
    hex_set = list(map(list, hex_set))

    dec = [0] * len(hex_set)
    for i in range(len(hex_set)):
        for j in range(n//4):
            if hex_set[i][j].isdecimal():
                dec[i] += (int(hex_set[i][j])) * 16**(n//4 - 1 - j)
            else:
                dec[i] += (ord(hex_set[i][j]) - 55) * 16**(n//4 - 1 - j)
    dec.sort(reverse=True)

    print(f'#{case}', dec[k-1])
