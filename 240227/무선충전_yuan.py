def location(i, j, n):
    if n == 0:
        return i, j
    if n == 1:
        return i, j - 1
    if n == 2:
        return i + 1, j
    if n == 3:
        return i, j + 1
    if n == 4:
        return i - 1, j


def findsum(ai, aj, bi, bj):
    A = []
    B = []
    for idx in range(bcnum):
        bci, bcj = bcij[idx][0], bcij[idx][1]
        if abs(ai - bci) + abs(aj - bcj) <= bc_range[idx]:
            A.append(idx)
        if abs(bi - bci) + abs(bj - bcj) <= bc_range[idx]:
            B.append(idx)

    maxsum = 0
    if A and not B:
        for i in A:
            sum = bc_charge[i]
            if sum > maxsum:
                maxsum = sum

    elif not A and B:
        for i in B:
            sum = bc_charge[i]
            if sum > maxsum:
                maxsum = sum

    elif A and B:
        for idxi in A:
            for idxj in B:
                sum = 0
                if idxi == idxj:
                    sum += bc_charge[idxi]

                elif idxi != idxj:
                    sum += bc_charge[idxi]
                    sum += bc_charge[idxj]

                if sum > maxsum:
                    maxsum = sum

    return maxsum


T = int(input())
for tc in range(1, T + 1):
    M, bcnum = map(int, input().split())
    ma = list(map(int, input().split()))  # a 이동정보
    mb = list(map(int, input().split()))  # b 이동정보

    # 나중에 루프 돌리면서 인덱스 맞추려고 넣어줌
    ma = [0] + ma
    mb = [0] + mb

    bcij = [0] * bcnum
    bc_range = [0] * bcnum  # 충전범위
    bc_charge = [0] * bcnum  # 충전량

    # m번째의 사용자 충전값 넣을 리스트
    usersum = [0] * (M + 1)

    for k in range(bcnum):
        i, j, r, c = map(int, input().split())
        bcij[k] = (i, j)
        bc_range[k] = r
        bc_charge[k] = c

    ai, aj = 1, 1
    bi, bj = 10, 10

    for i in range(M + 1):
        a1, a2 = location(ai, aj, ma[i])
        b1, b2 = location(bi, bj, mb[i])

        usersum[i] = findsum(a1, a2, b1, b2)

        ai, aj = a1, a2
        bi, bj = b1, b2
    # print(sum(usersum))
    print(f'#{tc} {sum(usersum)}')