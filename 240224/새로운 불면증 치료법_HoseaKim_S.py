# 새로운 불면증 치료법 (양 새기)
T = int(input())
for case in range(1, T+1):
    n = int(input())

    v = set()
    k = 0
    while len(v) < 10:
        k += 1
        v.update(set(map(int, str(n * k))))

    print(f'#{case}', n * k)
