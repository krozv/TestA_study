# 원자 소멸 시뮬레이션
"""
조건
원자들의 수 N 1<=N<=1000
보유에너지 K 1<=K<=100
처음위치 x, y -1000<=x,y<=1,000
이동방향 0, 1, 2, 3
원자 이동방향 변경 없음
"""
"""
# 완전검색
while문 사용 -> 원자가 1개도 남지 않을 때까지 반복 -> 시간초과 뜰 것 같은데
1초에 한번씩 전체 이동 확인
위치하려는 자리에 원자가 있을 경우 +1
1 이상인 원자 전부 삭제
원자가 한 개도 없을때까지 반복

def collide():
    pass
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0] * 2001 for _ in range(2001)]
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    atom = {}
    for i in range(N):
        x, y, d, K = map(int, input().split())
        atom[i+1] = [d, K]  # 원자번호를 key로 하여 delta와 K 보유에너지 저장
        arr[x+1000][y+1000] = -(i+1)    # -key를 저장
    print(atom)
    print(arr)
    energy = 0
    while sum(arr) != 0:
        collide()
    print(energy)
"""
"""
# greedy
원자 간의 거리가 제일 짧은 것 찾아서 충돌시키고 없앰
계속 돌려
제일 짧은 거 찾아서 충돌시키고 없앰
양방향을 굳이 봐야하나? -> 한줄씩 탐색
row:
    원자가 존재하고 and delta의 순서가 2, 3일 경우 충돌
col:
    원자가 존재하고 and delta의 순서가 0, 1일 경우 충돌
"""
def collide():
    pass
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    atom = {}
    for i in range(N):
        x, y, d, K = map(int, input().split())
        atom[i+1] = [[x, y], d, K]  # 원자번호를 key로 하여 delta와 K 보유에너지 저장
    print(atom)
    energy = 0
    while True:
        for i in range(N):
            print(atom[i+1][0])
    # print(energy)