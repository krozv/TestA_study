def dfs(x, ss):
    global min_cost
    if min_cost <= ss:
        return
    if x >= 12:
        if min_cost > ss:
            min_cost = ss
            return

    now_sum = 0
    for i in range(3):
        if x+i < 12:
            now_sum += plan[x+i] * ticket[x+i]

    if now_sum <= month_3:
        dfs(x + 1, ss + plan[x] * ticket[x])
    else:
        dfs(x + 3, ss + month_3)

    cnt = 0
    while cnt < 12 - x:
        cnt += 1
        dfs(x + cnt, ss + plan[x] * ticket[x])


def find_day_month():
    result = [day] * 12
    print(result)
    for i in range(12):
        if month_1 < plan[i] * day:
            result[i] = month_1
    return result


T = int(input())
for case in range(1, T+1):
    day, month_1, month_3, year = map(int, input().split())
    plan = list(map(int, input().split()))

    # 1일권 및 1달권 여부
    ticket = find_day_month()

    # 3달권 및 1년권 여부
    min_cost = year
    dfs(0, 0)

    print(f'#{case}', min_cost)
