'''
적은 비용으로 수영장 이용 방법을 찾는 중
이용권은 4종류
1. 1일 이용권
2. 1달 이용권 : 1달 동안 이용 가능. 1달 이용권은 매달 1일부터 시작
3. 3달 이용권 : 연속된 3달 이용 가능. 3달 이용권도 매달 1일부터 시작
4. 1년 이용권 : 1년 동안 이용 가능
이용 계획에 나타나는 숫자는 해당 달에 수영장을 이용할 날의 수를 의미
각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,
가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하시오.
'''

def health(m,cost): #m:선택할 달, cost:현재까지 이용권 합친 가격
    global min_sum_price
    if m > 12: #12월을 넘기는 경우
        if min_sum_price > cost:
            min_sum_price = cost
        return
    elif cost > min_sum_price: #중간에 그만 보고 돌아가
        return
    else:
        #1년 이용권으로 이용. 12달 후 상황판단
        health(m + 12, cost + prices[3])
        #3달 이용권으로 이용. 3달 후 상황판단
        health(m + 3, cost + prices[2])
        # 1달 이용권으로 이용. 1달 후 상황판단
        health(m+1, cost + prices[1])
        #1일 이용권으로 한달 이용. 1달 후 상황판단
        health(m+1, cost + prices[0]*plans[m])
        return

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))    #이용권 가격들
    plans = [0] + list(map(int, input().split()))    #[0] + 1개월 부터 12개월 이용계획
    min_sum_price =prices[3]*12 #당연히 연간이용권이 제일 비싸다고 생각했지만, 테스트케이스를 굉장히 독특하게 주면 틀릴 수도?
    health(1,0)
    print(f'#{tc} {min_sum_price}')