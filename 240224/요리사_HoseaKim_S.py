# 요리사
def permutation(i):
    global min_diff
    if i >= n-1:
        a = b = 0
        for r in range(n//2 - 1):
            for c in range(r+1, n//2):
                a += s[p[r]][p[c]]
                a += s[p[c]][p[r]]
                b += s[p[r-n//2]][p[c-n//2]]
                b += s[p[c-n//2]][p[r-n//2]]
        if min_diff > abs(a-b):
            min_diff = abs(a-b)
        return

    for j in range(i, n):
        p[i], p[j] = p[j], p[i]
        permutation(i+1)
        p[i], p[j] = p[j], p[i]


T = int(input())
for case in range(1, T+1):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]

    p = list(range(n))
    min_diff = 10**9
    permutation(0)

    print(f'#{case}', min_diff)
