# 1486. 장훈이의 높은 선반
### 코드
238ms

백트래킹 써서 풀이
```python
def make_top(i, top): #i는 사람 인덱스, top은 만들어진 탑 높이
    global min_top
    if i == N:
        if top >= B and min_top > top: #top이 선반 높이 이상이고 min_top보다
            min_top = top
        return
    if top > min_top: #백트래킹
        return
    #i번째 사람으로 탑 안 쌓기
    make_top(i+1, top)
    #i번째 사람으로 탑 쌓기
    make_top(i+1, top + height_list[i])

T = int(input())
for tc in range(1, 1+T):
    N, B = map(int, input().split()) #N은 사람 수,B는 선반 높이
    height_list = list(map(int, input().split())) #사람들 키 리스트
    min_top = sum(height_list)  # 최소 탑_높이(가능한 최댓값은 모든 사람들의 키 합)
    make_top(0, 0)
    print(f'#{tc} {min_top - B}')
```