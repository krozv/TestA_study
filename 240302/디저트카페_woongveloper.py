'''
카페간 이동은 대각선으로만 가능하다.
항상 사각형 모양을 이루는 경로로 돌아와야한다. (인덱스 항상 주의)
한 카페만 가거나 한줄로 코스를 세우는 경우는 없다.
또 같은 숫자가 적힌 카페에는 방문하지 않는다.
'''
'''
1. cafe_menu를 활용해 같은 메뉴를 파는 곳에 방문하지 않도록 한다.
2. 사각형을 이루는 조건 (방향성1 == 방향성1_rev, 방향성2 == 방향성2_rev)을 순열을 활용해 구할 수 있겠다.
    - 이 때 방향성은 대각선으로만 있다.
    - 시계방향 회전, 반시계방향 회전은 중요하지 않으므로, 정방향 리스트와 역방향 리스트를 만들어보자.

결국 디저트의 종류를 다양하게 먹는 것이 목적이므로 이를 활용해 경로를 구하고 이 경로의 길이를 출력한다.
'''
di = [-1,1,1,-1]
dj = [1,1,-1,-1]
# route = [slash_positive, rev_slash_positive, slash_negative, rev_slash_negative]
'''
정사각형의 변 길이만큼 slash, rev_slash이동이 가능하지만, 이 경우엔 한줄로만 이동이 가능하므로
최대 slash and rev_slash는 변 길이 -1 이다.
더불어 slash_positive + rev_slash_positive는 최대값이 변의 길이와 동일하다.
즉, 이동 경로의 최대값은 변의 두배와 동일하다는 것

따라서 최대 이동경로일 때 부터 경로 길이를 단축하며, 조건을 만족하는지 따진다.
positive길이와 negative길이는 같은값을 가져야한다.
'''
def dfs(n,lst):
    if n == 2:
        # 두개만 숫자를 뽑아도, slash, rev_slash방향 이동 길이 확인 가능
        if sum(lst) <= N:
            choose_route.append(lst * 2)
        return
    for i in range(1,N):
        dfs(n+1, lst+[i])

def can_i_move(route, start_i, start_j):
    visited = [0] * 101
    # visited[cafe_map[start_i][start_j]] = 1 # 시작지점 카페의 메뉴 기록
    now_i = start_i
    now_j = start_j
    for k in range(3): # 3개의 방향 고려, 0,1,2
        for i in range(1, route[k] + 1): # 각 방향별로 이동 얼마나 하나
            visited[cafe_map[now_i][now_j]] = 1
            move_i = now_i + di[k]
            move_j = now_j + dj[k]
            if 0<=move_i<=N-1 and 0<=move_j<=N-1 and visited[cafe_map[move_i][move_j]] == 0:
                # 인덱스를 만족하면서 이동이 가능하다면
                now_i = move_i
                now_j = move_j
                visited[cafe_map[now_i][now_j]] = 1
            else:
                return False
    for i in range(1, route[3]): # 각 방향별로 이동 얼마나 하나
        visited[cafe_map[now_i][now_j]] = 1
        move_i = now_i + di[3]
        move_j = now_j + dj[3]
        if 0<=move_i<=N-1 and 0<=move_j<=N-1 and visited[cafe_map[move_i][move_j]] == 0:
            # 인덱스를 만족하면서 이동이 가능하다면
            now_i = move_i
            now_j = move_j
            visited[cafe_map[now_i][now_j]] = 1
        else:
            return False
    return True

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    route_len_list = list(range(1,N))
    cafe_map = []
    for _ in range(N):
        cafe_map += [list(map(int,input().split()))]
    choose_route = []
    dfs(0,[])
    result = []
    for route in choose_route:
        for i in range(N):
            for j in range(N):
                if can_i_move(route, i, j) == True:
                    result.append(sum(route))
    if result == []:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {max(result)}")