for tc in range(1,11):
    # 테이블의 크기는 100*100
        # 각 테케의 첫 줄에는 한 변의 길이
    N = int(input())
    # 1은 N극 성질 2는 s극 성질을 가지는 자성체. 윗부분에는 N극이 아래부분이 S극이 있다.
    # 위에서부터 아래로, 아래에서부터 위로 점검하면서, 테이블과 반대극인 애들을 제거하자
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 교착상태를 체크할 카운터
    cnt = 0
    # 2를 만나면 제거 (0으로 바꿈) 1을 만나면 종료
    for j in range(N):
        i_1 = 0
        while i_1 < N and matrix[i_1][j] != 1:
            if matrix[i_1][j] == 2:
                matrix[i_1][j] = 0
            i_1 += 1

        i_2 = N-1
        while i_2 >= 0 and matrix[i_2][j] != 2:
            if matrix[i_2][j] == 1:
                matrix[i_2][j] = 0
            i_2 -= 1



    for j in range(N):
        # 스택을 써서 교착상태를 체크한다.
        st = []
        for i in range(N):
            if matrix[i][j] != 0:
                # 스택에 값이 존재하면
                if st:
                    # 가장 위의 값을 뺀다..
                    top = st.pop()
                    # 만약 넣으려는 값과 같으면

                    if top == matrix[i][j]:
                        # 둘 중 하나만 넣는다.
                        st.append(top)
                    else:
                        # 같지않으면, 값 둘다 넣는다.
                        st.append(top)
                        st.append(matrix[i][j])
                else: # 비어있는 경우 둘 다 넣는다.
                    st.append(matrix[i][j])
        cnt += len(st)//2
    print(f'#{tc} {cnt}')