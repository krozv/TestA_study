# start_a = [0, 0]
# start_b = [10, 10]
# dx = [0, 0, 1, 0, -1]
# dy = [0, -1, 0, 1, 0]

# T = iint(t)t(input())

# for tc in range(T):
#     m, a = map(int, input().split())

#     charger = {}
#     arr = [[[] for _ in range(10)] for _ in range(10)]

#     move_a = list(map(int, input().split()))
#     move_b = list(map(int, input().split()))

#     for i, _ in enumerate(range(a)):
#         x, y, c, p = map(int, input().split())
#         charger[i] = p
#         arr[y][x].append(i)
#         for i in range(1,5):
#             for j in range(1, c+1):
#                 mx = x + j * dx[i]
#                 my = y + j * dy[i]
#                 if 0 <= mx < 10 and 0 <= my < 10:
#                     arr[my][mx].append(i)

#     print(arr)



# # 1번 -> 위<->오
# # 2번 -> 아<->오
# # 3번 -> 왼<->아
# # 4번 -> 왼<->위
# # 5번 -> 모든 방향에서 방향이 반대로

# # 웜홀을 만나면 같은 번호의 웜홀로 위치 이동
# # 블랙홀


# import time

# # 방향을 정해줘야 함
# T = int(input())

# # 상, 하, 좌, 우
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# for tc in range(T):
#     n = int(input())
#     warm = [[] for _ in range(11)]
#     pin = []
#     score = 0

#     # 웜홀 위치 지정
#     for y in range(n):
#         pin.append(list(map(int, input().split())))
#         for x in range(n):
#             if pin[y][x] in [6,7,8,9,10]:
#                 warm[pin[y][x]].append([x,y])

#     # 전체 탐색
#     for y in range(n):
#         for x in range(n):
#             print('start',x, y)
#             start = [x,y] # 시작 위치 저장
#             for i in range(4): # 네 방향
#                 s = 0
#                 d = i
#                 print('d',d)
#                 while True:
#                     time.sleep(0.3)
#                     x += dx[d]
#                     y += dy[d]
#                     print(x,y)
#                     if x < 0 or x >= n or y < 0 or y >= n:
#                         x -= dx[d]
#                         y -= dy[d]
#                         s += 1
#                         if d == 0:
#                             d = 1
#                         elif d == 1:
#                             d = 0
#                         elif d == 2:
#                             d = 3
#                         else:
#                             d = 2
#                         continue

#                     # 종료 조건
#                     if [x,y] == start or pin[y][x] == -1 or :
#                         break

#                     if pin[y][x] == 1:
#                         s += 1
#                         if d == 0:
#                             d = 1
#                         elif d == 1:
#                             d = 3
#                         elif d == 2:
#                             d = 0
#                         else:
#                             d = 2
#                     elif pin[y][x] == 2:
#                         s += 1
#                         if d == 0:
#                             d = 3
#                         elif d == 1:
#                             d = 0
#                         elif d == 2:
#                             d = 1
#                         else:
#                             d = 2
#                     elif pin[y][x] == 3:
#                         s += 1
#                         if d == 0:
#                             d = 2
#                         elif d == 1:
#                             d = 0
#                         elif d == 2:
#                             d = 3
#                         else:
#                             d = 1
#                     elif pin[y][x] == 4:
#                         s += 1
#                         if d == 0:
#                             d = 1
#                         elif d == 1:
#                             d = 2
#                         elif d == 2:
#                             d = 3
#                         else:
#                             d == 0
#                     elif pin[y][x] == 5:
#                         s += 1
#                         if d == 0:
#                             d = 1
#                         elif d == 1:
#                             d = 0
#                         elif d == 2:
#                             d = 3
#                         else:
#                             d = 2
#                     elif pin[y][x] in [6,7,8,9,10]:
#                         x, y = warm[pin[y][x]].remove([x,y])

#                 if s > score:
#                     score = s

#     print(f'#{tc+1} {score}')
