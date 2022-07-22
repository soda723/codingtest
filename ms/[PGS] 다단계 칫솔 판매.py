#### 테케는 다 맞는데 채점해보면 다 틀리는 이유는????

# enroll = 각 판매원의 이름(center 이름은 없음)
# referral = 각 판매원의 추천인
# seller = 판매량에 대한 판매원의 이름
# amount = 판매량
def solution(enroll, referral, seller, amount):
    amount = [i * 100 for i in amount]
    answer = [0 for i in enroll]

    # enroll의 추천인 인덱스 배열 rindex -> 예시 [0, 0, 1, 2, 1, 1, 5, 2]
    rindex = []
    for i in range(len(enroll)):
        if referral[i] != '-':
            rindex.append(enroll.index(referral[i]))
        else:
            rindex.append(0)

    """
    판매원 young의 경우
    반복 1 -> staff = 7, money = 1200, boss = 2, answer[7] += 1080
    반복 2 -> money = 120, staff = 2, boss = 1, answer[2] += 108
    반복 3 -> money = 12, staff = 1, boss = 0(break문)
    이런 식으로 풀었음!
    """
    for i in range(len(seller)):
        staff = enroll.index(seller[i])
        money = amount[i]

        while True:
            answer[staff] += (money - money // 10)
            boss = rindex[staff]

            if boss == 0:
                break
            
            money = money // 10
            staff = boss
    
    return answer
