# 새로운 불면증 치료법
"""

"""
T = int(input())
for t in range(1, T+1):
    N = input()
    a = list(map(str, range(0, 10)))
    i = 1
    while a:
        lst_n = list(str(int(N) * i))
        for num in lst_n:
            if num in a:
                a.remove(num)
        i += 1
    print(f'{t} {int(N) * (i-1)})
