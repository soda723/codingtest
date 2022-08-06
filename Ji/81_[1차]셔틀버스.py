# 소요시간 : 1h 22m ~~ing
# 시간 비교하는게 너무 어렵다.
# 푸는 중
from datetime import datetime
def get_lastbus(n,t):
    # 막차시간 계산
    if t == 1:
        answer = "09:00"
    elif t<60:
        hour = n*t // 60
        minute = n*t-hour
        if hour == 0 :
            hour = "09"
        else :
            if hour > 9 : hour = str(9 + hour - 1)
            else : hour = "0" + str(9 + hour - 1)
        answer = hour +":"+ str(minute-t)
    else : # t==60
        hour = n*t // 60
        if hour == 0 :
            hour = "09"
        else :
            if hour > 9 : hour = str(9 + hour - 1)
            else : hour = "0" + str(9 + hour - 1)
        answer = hour +":00"
    print(answer)
    return answer

def get_thistime(stime, t):
    # 이렇게 계산하면 안됌
    # t1 = datetime.strptime(stime, "%H:%M")
    # t2 = datetime.strptime(t, "%M")
    return t1+t2
    
def solution(n, t, m, timetable):
    #answer를 막차시간으로 초기화
    answer = get_lastbus(n,t)

    # 오는 사람이 최대 인원보다 작으면 막차타면됌.
    if len(timetable)  < m :
        return answer
    
    # 사람을 순서대로 정렬하기
    ntimetable = list(timetable.sort(key=lambda x: datetime.datetime.strptime(x, '%H:%M')))

    ## 여기부터 완성 X 수도코드느낌으로 작성되어있음 
    # 첫차시간부터 계산 해서 막차에 남은 사람만 남기기 (하는중 ... )[0909 0910]
    cnt_m = m
    cnt_t = t
    while t > 0:
        nextlist = []
        #thistime = 계산
        for time in ntimetable:
            if time > thistime:
                nextlist.append(time)
            m -= 1
            if m == 0 : break
               
        cnt_t -= 1
        ntimetable = nextlist # 남은사람들 다음으로
    ## case1 :  남은 사람이 정원보다 적으면 막차시간에 온다
    if len(ntimetable) <= m : return answer
    ## case2 : 제일 빨리 온 사람이 버스 도착시간보다 늦게 올때(예제6) 막차시간에 온다
    elif ntimetable[0] > bustime : return answer
    ## case 3 : m번째 사람보다 1분 빠르게 온다.
    else: 
        #answer = new[m-1] - 1분
        return answer
    #end solution

#print(str(get_thistime("09:00", str(10))))