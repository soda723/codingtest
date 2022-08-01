def calculate(staff, money, pyramid, answer):
    answer[staff] += money - money // 10

    # 아래 조건 추가 안해주면 재귀 단계 때문에 런타임 에러
    if money == 0:
        return
    
    if pyramid[staff] == '-':
        return
    else:
        calculate(pyramid[staff], money // 10, pyramid, answer)


def solution(enroll, referral, seller, amount):
    pyramid = {}
    answer = {}
    final = []

    # {판매원: 추천인} 형태의 딕셔너리 만들기
    for i in range(len(enroll)):
        pyramid[enroll[i]] = referral[i]
        answer[enroll[i]] = 0

    # 판매 기록에 따라 판매 금액 계산하는 함수 호출
    for i in range(len(seller)):
        money = amount[i] * 100
        calculate(seller[i], money, pyramid, answer)

    # 딕셔너리를 리스트 형태로 바꿔주기
    for i in range(len(enroll)):
        final.append(answer[enroll[i]])


    return final

