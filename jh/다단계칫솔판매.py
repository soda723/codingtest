def solution(enroll, referral, seller, amount):
    answer = {i:0 for i in enroll}
    refe = {enroll[i]: referral[i] for i in range(len(enroll))}

    # 딕셔너리로 수익을 저장하면 john의 수익이 두 번에 나누어 들어올 경우 값이 합쳐지기 때문에 쓰면 안 됨
    # profit = {i: 0 for i in enroll}
    # for i in range(len(seller)):
    #     profit[seller[i]] = 100 * amount[i]
        
    for k, a in zip(seller, amount):
        v = 100 * a
        while True:
            if v == 0:
                break
            m = v // 10
            answer[k] += v - m
            re = refe[k]
            if re == '-':
                break
            k = re
            v = m
            
    return list(answer.values())