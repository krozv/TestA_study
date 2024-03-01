# 숫자 만들기 SWEA 4008
'''
def permutation(i):
    global max_ss
    global min_ss
    if i == n-2:
        ss = num[0]
        for j in range(n-1):
            if p[j] == 0:
                ss += num[j+1]
            elif p[j] == 1:
                ss -= num[j+1]
            elif p[j] == 2:
                ss *= num[j+1]
            elif p[j] == 3:
                if ss < 0:
                    ss = -(-ss//num[j+1])
                else:
                    ss //= num[j+1]
        if max_ss < ss:
            max_ss = ss
        if min_ss > ss:
            min_ss = ss
        return
    for j in range(i, n-1):
        if i != j and p[i] == p[j]:
            continue
        p[i], p[j] = p[j], p[i]
        permutation(i+1)
        p[i], p[j] = p[j], p[i]


T = int(input())
for case in range(1, T+1):
    # 숫자 개수
    n = int(input())
    # + - * / 각 개수 (총 n-1개)
    op = list(map(int, input().split()))
    # 숫자들
    num = list(map(int, input().split()))

    max_ss = -10**9
    min_ss = 10**9
    p = [0]*op[0] + [1]*op[1] + [2]*op[2] + [3]*op[3]
    permutation(0)

    print(f'#{case}', max_ss - min_ss)
'''


def permutation(i, ss):
    global max_ss
    global min_ss
    if i >= n-1:
        if max_ss < ss:
            max_ss = ss
        if min_ss > ss:
            min_ss = ss
    for j in range(4):
        if op[j]:
            if j == 0:
                op[j] -= 1
                permutation(i+1, ss + num[i+1])
                op[j] += 1
            elif j == 1:
                op[j] -= 1
                permutation(i+1, ss - num[i+1])
                op[j] += 1
            elif j == 2:
                op[j] -= 1
                permutation(i+1, ss * num[i+1])
                op[j] += 1
            elif j == 3:
                op[j] -= 1
                if ss < 0:
                    permutation(i+1, -(-ss // num[i+1]))
                else:
                    permutation(i+1, ss // num[i+1])
                op[j] += 1


T = int(input())
for case in range(1, T+1):
    # 숫자 개수
    n = int(input())
    # + - * / 각 개수 (총 n-1개)
    op = list(map(int, input().split()))
    # 숫자들
    num = list(map(int, input().split()))

    max_ss = -10**9
    min_ss = 10**9
    permutation(0, num[0])

    print(f'#{case}', max_ss - min_ss)
