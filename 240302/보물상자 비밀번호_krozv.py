# 보물상자 비밀번호
"""
8 <= N <= 28
0 <= Nij <= F
큐 만들어서 돌려. N//4만큼 끊어. K번째 인덱스 출력해
N// 4만큼만 돌리면 반복됨
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    num = []
    for _ in range(N//4):
        # print(arr)
        for i in range(0, N, N//4):
            num.append(''.join(arr[i:i+N//4]))
        l = arr.pop()
        arr = [l] + arr
    # print(num)
    num = list(set(num))
    num = list(map(lambda x: int(x, 16), num))
    num.sort(reverse=True)
    print(f'#{t} {num[K-1]}')