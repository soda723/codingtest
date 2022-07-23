#40m / 시간초과 힌트 * list.index 대신 dict 사용하기
def tax_cal(dict_enroll, referral, money, answer,idx):
    upmoney = int(money*0.1) # 상부에 줘야할 돈
    answer[idx]+= money-upmoney # 내 이익금 = 칫솔판매액-상부납부액
    ref = referral[idx] # 직속상사 찾기
    if upmoney == 0: # 납부액이 0원이면 그만
        return None
    if ref == '-' : # 상부없으면 그만
        return None
    else :
        tax_cal(dict_enroll,referral, upmoney,answer,dict_enroll[ref])
    
    
def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll) # 수익금 담을 리스트
    dict_enroll = {name:i for i, name in enumerate(enroll)} # enroll 딕셔너리로 만들기 idx 접근 빠르게 하기 위함
    for idx, name in enumerate(seller):
        money = amount[idx]*100 #칫솔개수*100원
        name_idx = dict_enroll[name] 
        tax_cal(dict_enroll, referral, money, answer, name_idx)
    
    return answer