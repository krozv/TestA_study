# dfs 로 각 조에 한명씩 N번 반복해서 넣어주는 여러 경우
def dfs(current, i):
    global min_sum
    if i == N:
        suma = 0
        sumb = 0
        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                suma += arr[A[i] - 1][A[j] - 1] + arr[A[j] - 1][A[i] - 1]
                sumb += arr[B[i] - 1][B[j] - 1] + arr[B[j] - 1][B[i] - 1]

        min_sum = min(min_sum, abs(suma - sumb))
        return
    else:
        if len(A) < N // 2:  # 두명
            A.append(current)
            dfs(current + 1, i + 1)
            A.pop()

        if len(B) < N // 2:
            B.append(current)
            dfs(current + 1, i + 1)
            B.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = []
    B = []
    min_sum = 100000000000000000
    dfs(1, 0)  # 현재 번호, 카운트 수
    print(f'#{tc} {min_sum}')