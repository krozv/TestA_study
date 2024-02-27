# 무선충전
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    M, BC = map(int, input().split())   # M: 이동 시간, BC: 배터리 개수
    A_lst = [0] + list(map(int, input().split())) # A 이동경로
    B_lst = [0] + list(map(int, input().split())) # B 이동경로
    bc_lst = []
    for bc in range(BC):
        X, Y, C, P = map(int, input().split())
        # 충전기 범위 딕셔너리 생성하기
        # bc_lst[i] = {좌표: Power}
        bcl = []
        for i in range(11):
            for j in range(11):
                if abs(X-i) + abs(Y-j) <= C:
                    bcl.append((i, j))
        bc_lst.append([bcl, P])
    # 시간에 따른 A와 B 이동
    Ax = 1
    Ay = 1
    Bx = By = 10
    # 이동방향
    d = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
    charge = 0
    for i in range(M+1):
        dA = A_lst[i]
        A_BC = []
        Ax = Ax + d[dA][0]
        Ay = Ay + d[dA][1]
        for j in range(BC):
            if (Ax, Ay) in bc_lst[j][0]:
                A_BC.append(j)

        dB = B_lst[i]
        B_BC = []
        Bx = Bx + d[dB][0]
        By = By + d[dB][1]
        for j in range(BC):
            if (Bx, By) in bc_lst[j][0]:
                B_BC.append(j)
        # 교집합 있을때
        if set(A_BC) & set(B_BC):
            interset = set(A_BC) & set(B_BC)
            A_set = set(A_BC) - interset
            B_set = set(B_BC) - interset
            # A_set와 B_set가 없을 때
            if not A_set and not B_set:
                # interset의 길이가 2개 이상
                power_lst = []
                if len(interset) > 1:
                    # print('교집합있음, A, B 없음')
                    for s in interset:
                        power_lst.append(bc_lst[s][1])
                    power_lst.sort(reverse=True)
                    charge += power_lst[0]
                    charge += power_lst[1]
                # interset의 길이가 1개 미만
                else:
                    # print('교집합있음, A, B 없음, 길이 1개')
                    interset = list(interset)
                    charge += bc_lst[interset[0]][1]
            # A_set만 없을 때
            elif not A_set:
                # print('교집합있음, A만 없음')
                power_B = []
                power_I = []
                for s in B_set:
                    power_B.append(bc_lst[s][1])
                for s in interset:
                    power_I.append(bc_lst[s][1])
                power_I.append(max(power_B))
                power_I.sort(reverse=True)
                charge += power_I[0]
                charge += power_I[1]
            # B_set만 없을 때
            elif not B_set:
                # print('교집합있음, B만 없음')
                power_A = []
                power_I = []
                for s in A_set:
                    power_A.append(bc_lst[s][1])
                for s in interset:
                    power_I.append(bc_lst[s][1])
                power_I.append(max(power_A))
                power_I.sort(reverse=True)
                charge += power_I[0]
                charge += power_I[1]
            # A_set와 B_Set 둘다 존재
            else:
                # print('교집합있음, A, B 둘다있음')
                power_A = []
                power_B = []
                power_I = []
                for s in A_set:
                    power_A.append(bc_lst[s][1])
                for s in B_set:
                    power_B.append(bc_lst[s][1])
                for s in interset:
                    power_I.append(bc_lst[s][1])
                power_I.append(max(power_A))
                power_I.append(max(power_B))
                power_I.sort(reverse=True)
                charge += power_I[0]
                charge += power_I[1]
        # 교집합 없을때
        else:
            # print('교집합없음')
            A_set = set(A_BC)
            B_set = set(B_BC)
            power_lst = []
            if A_set:
                for s in A_set:
                    power_lst.append(bc_lst[s][1])
                power_lst.sort(reverse=True)
                charge += power_lst[0]
            power_lst = []
            if B_set:
                for s in B_set:
                    power_lst.append(bc_lst[s][1])
                power_lst.sort(reverse=True)
                charge += power_lst[0]
    print(f'#{t} {charge}')